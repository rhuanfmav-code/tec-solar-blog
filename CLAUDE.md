# Instruções permanentes

Sempre faça commit e push diretamente na branch main.
Nunca crie branches separadas.
Nunca abra Pull Requests.
Trabalhe sempre na main diretamente.

## Regras obrigatórias de git para geração de posts

- Antes de qualquer commit, execute `git checkout main` para garantir que está na branch correta.
- Se o repositório estiver em outra branch, retorne para a main com `git checkout main` antes de escrever qualquer arquivo.
- Nunca commite posts, prompts de carrossel ou atualizações do progresso.md em branches intermediárias.
- O fluxo correto é: escrever arquivo → `git add` → `git commit` → `git push origin main`.
- Se o ambiente de sessão criar uma branch automática (ex: claude/alguma-branch), ignore-a e trabalhe na main mesmo assim.
- Nunca faça merge de branches — os arquivos já devem nascer na main.

## Regra obrigatória de título dos posts

O título enviado ao WordPress NUNCA deve incluir o prefixo "Post XX —", "Post XX -" ou "Post XX:".
O título publicado deve começar diretamente com o tema técnico.

Exemplos:
- ERRADO: `Post 05 — Sungrow Grid Lost: Perda de Rede`
- CORRETO: `Sungrow Grid Lost: Perda de Rede — Causa e Diagnóstico`

Regras de aplicação:
- O H1 do arquivo .md pode manter o prefixo "Post XX —" para organização interna do repositório.
- O campo `[TÍTULO SEO — Title Tag]` jamais deve conter o prefixo — é esse campo que vai para o WordPress como título.
- O script `publicar_wordpress.py` remove o prefixo automaticamente via regex antes de publicar,
  cobrindo os formatos: `Post XX —`, `Post XX -` e `Post XX:` (com ou sem espaços).
- Essa remoção é uma camada de segurança — o título já deve estar limpo no campo SEO.
