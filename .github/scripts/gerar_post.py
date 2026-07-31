#!/usr/bin/env python3
"""
Geração automática do próximo post do blog TEC Solar.

Fluxo:
  1. Descobre o próximo post ainda não gerado (maior posts/post-XX.md existente + 1).
  2. Lê o tema desse post no calendário editorial dentro de prompt.md.
  3. Chama a API do Claude usando prompt.md como instrução (system) e um post
     recente como exemplo de formato, seguindo Etapa 1 (rascunho) + Etapa 2
     (Humanizer) + Etapa 3 (output com todos os campos).
  4. Grava posts/post-XX.md no formato exato que publicar_wordpress.py parseia.
  5. Atualiza progresso.md.

O workflow (gerar-post-diario.yml) faz o commit e o push.
A publicação no WordPress fica por conta do workflow separado publicar_wordpress.yml.

Requisitos:
  pip install anthropic
  Secret ANTHROPIC_API_KEY no repositório.
"""

import os
import re
import sys
from pathlib import Path

import anthropic

RAIZ = Path(__file__).resolve().parents[2]
DIR_POSTS = RAIZ / "posts"
ARQ_PROMPT = RAIZ / "prompt.md"
ARQ_PROGRESSO = RAIZ / "progresso.md"

MODELO = os.environ.get("MODELO_GERACAO", "claude-sonnet-5")
MAX_TOKENS = int(os.environ.get("MAX_TOKENS_GERACAO", "8000"))


def proximo_numero() -> int:
    """Maior post-XX.md existente + 1."""
    numeros = []
    for arq in DIR_POSTS.glob("post-*.md"):
        m = re.search(r"post-0*(\d+)\.md$", arq.name)
        if m:
            numeros.append(int(m.group(1)))
    return (max(numeros) + 1) if numeros else 1


def tema_do_calendario(prompt_txt: str, numero: int) -> str | None:
    """Extrai a linha 'Post N — tema' do calendário em prompt.md."""
    padrao = rf"^Post\s+0*{numero}\s+[—\-:]\s*(.+)$"
    m = re.search(padrao, prompt_txt, re.MULTILINE)
    return m.group(1).strip() if m else None


def carregar_exemplo() -> str:
    """Usa o post gerado mais recente como referência de formato."""
    candidatos = sorted(
        DIR_POSTS.glob("post-*.md"),
        key=lambda p: int(re.search(r"post-0*(\d+)\.md$", p.name).group(1)),
        reverse=True,
    )
    for arq in candidatos:
        texto = arq.read_text(encoding="utf-8")
        # Só serve de exemplo se estiver completo (tem corpo humanizado real).
        if "[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]" in texto and len(texto) > 3000:
            return texto
    raise RuntimeError("Nenhum post completo encontrado para servir de exemplo de formato.")


def gerar(numero: int, tema: str, prompt_txt: str, exemplo: str) -> str:
    cliente = anthropic.Anthropic()

    instrucao = f"""Gere AGORA o Post {numero} do blog da TEC Solar.

TEMA DO POST {numero} (do calendário editorial): {tema}

Siga rigorosamente o processo definido nas instruções do sistema:
- ETAPA 1: rascunho técnico completo na estrutura correta.
- ETAPA 2: aplique TODO o processo Humanizer (Passos 2A, 2B, 2C).
- ETAPA 3: entregue o output com TODOS os campos.

REGRAS DE FORMATO — OBRIGATÓRIAS (o arquivo é parseado por script):
- A saída deve ser SOMENTE o conteúdo do arquivo .md. Sem preâmbulo, sem comentários,
  sem blocos de código markdown envolvendo tudo.
- Primeira linha exatamente: `# Post {numero} — <título interno>`
- Use os campos entre colchetes EXATAMENTE com estes rótulos, cada um seguido do
  conteúdo e separado por uma linha `---`, na mesma ordem e formato do EXEMPLO abaixo:
  [PALAVRA-CHAVE FOCO], [TÍTULO SEO — Title Tag], [SLUG — URL do Post],
  [META DESCRIPTION], [CATEGORIA], [TAGS], [TEXTO DO POST — VERSÃO HUMANIZADA FINAL],
  depois o bloco CTA HTML, depois [LINKS INTERNOS SUGERIDOS], [LINKS EXTERNOS SUGERIDOS],
  [IMAGEM PRINCIPAL — USE ESTA], [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST].
- O [TÍTULO SEO — Title Tag] NÃO pode conter o prefixo "Post {numero} —".
- O bloco CTA HTML (div com os três botões WhatsApp/Instagram/YouTube) deve ser
  copiado EXATAMENTE como no exemplo, sem alterar links.
- Corpo do post entre 900 e 1200 palavras.
- Só insira links internos reais para posts que existam; na dúvida, deixe a âncora
  sem link (o texto corre normalmente).

EXEMPLO DE FORMATO (estrutura e campos — NÃO copie o conteúdo técnico, só o formato):

{exemplo}

Agora gere o Post {numero} sobre o tema indicado, no MESMO formato."""

    resposta = cliente.messages.create(
        model=MODELO,
        max_tokens=MAX_TOKENS,
        system=[
            {
                "type": "text",
                "text": prompt_txt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": instrucao}],
    )

    partes = [b.text for b in resposta.content if getattr(b, "type", None) == "text"]
    saida = "".join(partes).strip()

    # Remove cercas de código se o modelo envolver tudo em ```.
    if saida.startswith("```"):
        saida = re.sub(r"^```[a-zA-Z]*\n", "", saida)
        saida = re.sub(r"\n```\s*$", "", saida)

    return saida.strip() + "\n"


def validar(texto: str, numero: int) -> None:
    obrigatorios = [
        f"# Post {numero}",
        "[PALAVRA-CHAVE FOCO]",
        "[TÍTULO SEO — Title Tag]",
        "[SLUG — URL do Post]",
        "[META DESCRIPTION]",
        "[CATEGORIA]",
        "[TAGS]",
        "[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]",
    ]
    faltando = [m for m in obrigatorios if m not in texto]
    if faltando:
        raise RuntimeError(f"Post gerado sem os campos obrigatórios: {faltando}")


def atualizar_progresso(numero: int) -> None:
    conteudo = (
        "# Controle de Posts Gerados\n\n"
        f"Último post gerado: Post {numero}\n\n"
        f"Posts gerados até agora: Posts 01 a {numero}\n\n"
        f"Próximo post a gerar: Post {numero + 1}\n"
    )
    ARQ_PROGRESSO.write_text(conteudo, encoding="utf-8")


def main() -> int:
    numero = proximo_numero()
    arquivo = DIR_POSTS / f"post-{numero:02d}.md"

    if arquivo.exists():
        print(f"Post {numero} já existe ({arquivo.name}). Nada a gerar.")
        return 0

    prompt_txt = ARQ_PROMPT.read_text(encoding="utf-8")
    tema = tema_do_calendario(prompt_txt, numero)
    if not tema:
        print(
            f"Post {numero} não está no calendário editorial de prompt.md. "
            "Calendário esgotado — adicione novos temas antes de gerar."
        )
        return 0

    print(f"Gerando Post {numero}: {tema}")
    exemplo = carregar_exemplo()
    texto = gerar(numero, tema, prompt_txt, exemplo)
    validar(texto, numero)

    arquivo.write_text(texto, encoding="utf-8")
    atualizar_progresso(numero)
    print(f"Post {numero} gravado em {arquivo.relative_to(RAIZ)} "
          f"({len(texto.split())} palavras no arquivo).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
