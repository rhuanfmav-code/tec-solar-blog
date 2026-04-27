"""
TEC Solar — Atualiza CTA nos posts 02-27 já publicados no WordPress.

Substitui o bloco CTA antigo ("Condenaram seu inversor...") pelo novo
bloco com links reais para WhatsApp, Instagram e YouTube.
Usa context=edit para obter o conteúdo raw e evitar double-encoding.
"""

import os
import re
import json
import sys
import requests
from pathlib import Path

WP_URL      = os.environ.get("WP_URL", "https://blogtecsolar.com.br").rstrip("/")
WP_USER     = os.environ.get("WP_USER", "")
WP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")
AUTH        = (WP_USER, WP_PASSWORD)
API_BASE    = f"{WP_URL}/wp-json/wp/v2"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

NEW_CTA_SENTINEL = "background:#25D366"  # exclusivo dos botões novos
OLD_CTA_MARKERS  = ["Condenaram seu inversor", "Antes de comprar equipamento novo"]

CTA_HTML = (
    "<hr>\n"
    "<h2>Envie seu inversor para diagnóstico</h2>\n"
    "<p>Antes de comprar equipamento novo, envie para a nossa bancada. "
    "A TEC Solar realiza diagnóstico eletrônico completo em nível de componente "
    "— abrimos o inversor, medimos a placa, identificamos a causa raiz e "
    "entregamos um laudo técnico detalhado.</p>\n"
    "<p>Se o reparo for viável, você recebe o equipamento funcionando por uma "
    "fração do custo de substituição. Se não for, o laudo serve de base para "
    "qualquer decisão.</p>\n"
    "<p>Atendemos todo o Brasil via logística reversa.</p>\n"
    '<div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">\n'
    "<a href=\"https://wa.me/5538998891587?text=Ol%C3%A1%2C%20vim%20pelo%20blog%20e%20quero%20enviar%20meu%20inversor%20para%20diagn%C3%B3stico\" "
    'target="_blank" style="background:#25D366; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "👉 Falar no WhatsApp agora</a>\n"
    "<a href=\"https://www.instagram.com/tec_solar_moc?igsh=MWl2djYzeXk2Zm51dQ%3D%3D&utm_source=qr\" "
    'target="_blank" style="background:#E1306C; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "📸 Seguir no Instagram</a>\n"
    "<a href=\"https://youtube.com/@tecsolar-reparodeinversores?si=kG3Njqipg8QRbZSD\" "
    'target="_blank" style="background:#FF0000; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "▶️ Ver vídeos no YouTube</a>\n"
    "</div>"
)


def extrair_slug(caminho_md: Path) -> str:
    texto = caminho_md.read_text(encoding="utf-8")
    m = re.search(r"\[SLUG[^\]]*\]\s*\n+\s*\n+(.+?)(?:\n|$)", texto)
    return m.group(1).strip() if m else ""


def buscar_post_por_slug(slug: str):
    """Retorna (post_id, raw_content) ou (None, None). Usa context=edit."""
    resp = requests.get(
        f"{API_BASE}/posts",
        auth=AUTH,
        params={"slug": slug, "status": "any", "context": "edit",
                "_fields": "id,content,link"},
        timeout=30,
    )
    if not resp.ok:
        print(f"   Erro HTTP {resp.status_code} ao buscar '{slug}'")
        return None, None
    posts = resp.json()
    if not posts:
        print(f"   Não encontrado no WordPress: '{slug}'")
        return None, None
    post = posts[0]
    # context=edit retorna content.raw; fallback para rendered
    content_obj = post.get("content", {})
    raw = content_obj.get("raw") or content_obj.get("rendered", "")
    return post["id"], raw


def substituir_cta(html: str):
    """
    Retorna novo HTML com CTA atualizado, ou None se já estiver correto.
    - Se background:#25D366 estiver presente → botões novos já existem, pular
    - Caso contrário → remover CTA antigo (qualquer variante) e injetar novo
    """
    if NEW_CTA_SENTINEL in html:
        return None

    # Localiza início do CTA antigo pelo primeiro marcador encontrado
    idx_old = -1
    for marker in OLD_CTA_MARKERS:
        pos = html.find(marker)
        if pos != -1:
            idx_old = pos
            break

    if idx_old != -1:
        idx_hr = html.rfind("<hr>", 0, idx_old)
        corte  = idx_hr if idx_hr != -1 else idx_old
        html   = html[:corte].rstrip()

    return html + "\n" + CTA_HTML


def atualizar_post(post_id: int, novo_conteudo: str) -> bool:
    resp = requests.post(
        f"{API_BASE}/posts/{post_id}",
        auth=AUTH,
        data=json.dumps({"content": novo_conteudo}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=30,
    )
    if not resp.ok:
        print(f"   Erro HTTP {resp.status_code}: {resp.text[:300]}")
    return resp.ok


def main():
    if not WP_USER or not WP_PASSWORD:
        print("ERRO: defina WP_USER e WP_APP_PASSWORD como variáveis de ambiente.")
        sys.exit(1)

    posts_dir = REPO_ROOT / "posts"
    ok = ja_ok = nao_encontrado = erro = 0

    for num in range(2, 28):
        caminho = posts_dir / f"post-{num:02d}.md"
        if not caminho.exists():
            print(f"[{num:02d}] arquivo local não encontrado — pulando")
            nao_encontrado += 1
            continue

        slug = extrair_slug(caminho)
        if not slug:
            print(f"[{num:02d}] slug vazio — pulando")
            erro += 1
            continue

        print(f"\n[{num:02d}] slug={slug}")
        post_id, conteudo_atual = buscar_post_por_slug(slug)
        if post_id is None:
            nao_encontrado += 1
            continue

        novo = substituir_cta(conteudo_atual)
        if novo is None:
            print(f"   ✓ CTA já atualizado (ID {post_id})")
            ja_ok += 1
            continue

        if atualizar_post(post_id, novo):
            print(f"   ✓ Atualizado (ID {post_id})")
            ok += 1
        else:
            erro += 1

    print(f"\n{'='*40}")
    print(f"Atualizados agora : {ok}")
    print(f"Já com novo CTA   : {ja_ok}")
    print(f"Não encontrados   : {nao_encontrado}")
    print(f"Erros             : {erro}")


if __name__ == "__main__":
    main()
