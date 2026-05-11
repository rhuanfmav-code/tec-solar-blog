"""
TEC Solar — Deleta posts duplicados no WordPress.

Identifica slugs com sufixo numérico (-2, -3...) que correspondem a um slug
original já existente. Para cada duplicata, deleta o post de maior ID (mais
recente), preservando o original (menor ID).

Uso:
  python3 deletar_duplicatas.py            # deleta de verdade
  python3 deletar_duplicatas.py --dry-run  # apenas lista, sem deletar
"""

import os
import re
import sys
import requests

WP_URL      = os.environ.get("WP_URL", "https://blogtecsolar.com.br").rstrip("/")
WP_USER     = os.environ.get("WP_USER", "")
WP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")
AUTH        = (WP_USER, WP_PASSWORD)
API_BASE    = f"{WP_URL}/wp-json/wp/v2"


def listar_todos_posts():
    posts = []
    page  = 1
    while True:
        resp = requests.get(
            f"{API_BASE}/posts",
            auth=AUTH,
            params={
                "status":   "any",
                "per_page": 100,
                "page":     page,
                "_fields":  "id,slug,link,date",
            },
            timeout=30,
        )
        if not resp.ok:
            print(f"Erro HTTP {resp.status_code} ao listar posts (página {page})")
            break
        batch = resp.json()
        if not batch:
            break
        posts.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return posts


def identificar_duplicatas(posts):
    """
    Agrupa posts pelo slug-base (sem sufixo numérico final).
    Ex: 'growatt-erro-102' e 'growatt-erro-102-2' → mesmo grupo.
    Retorna lista de posts a deletar (todos exceto o de menor ID).
    """
    grupos = {}
    for post in posts:
        base = re.sub(r'-\d+$', '', post["slug"])
        grupos.setdefault(base, []).append(post)

    duplicatas = []
    for base, grupo in grupos.items():
        if len(grupo) < 2:
            continue
        grupo_sorted = sorted(grupo, key=lambda p: p["id"])
        original = grupo_sorted[0]
        for dup in grupo_sorted[1:]:
            duplicatas.append({
                "id":       dup["id"],
                "slug":     dup["slug"],
                "link":     dup.get("link", ""),
                "original": original["slug"],
                "orig_id":  original["id"],
            })
    return duplicatas


def deletar_post(post_id):
    resp = requests.delete(
        f"{API_BASE}/posts/{post_id}",
        auth=AUTH,
        params={"force": "true"},
        timeout=30,
    )
    return resp.ok, resp.status_code


def main():
    if not WP_USER or not WP_PASSWORD:
        print("ERRO: WP_USER e WP_APP_PASSWORD são obrigatórios.")
        sys.exit(1)

    dry_run = "--dry-run" in sys.argv

    print("Buscando todos os posts no WordPress...")
    posts = listar_todos_posts()
    print(f"Total encontrado: {len(posts)} posts\n")

    duplicatas = identificar_duplicatas(posts)

    if not duplicatas:
        print("Nenhuma duplicata encontrada.")
        return

    print(f"{len(duplicatas)} duplicata(s) identificada(s):")
    for d in duplicatas:
        print(
            f"  [ID {d['id']}] {d['slug']}"
            f"  ← duplicata de [{d['orig_id']}] {d['original']}"
            f"  {d['link']}"
        )

    if dry_run:
        print("\n[DRY RUN] Nenhuma exclusão realizada.")
        return

    print("\nDeletando duplicatas (force=true)...")
    ok = erro = 0
    for d in duplicatas:
        sucesso, status = deletar_post(d["id"])
        if sucesso:
            print(f"  DELETADO: ID {d['id']} — {d['slug']}")
            ok += 1
        else:
            print(f"  ERRO ao deletar ID {d['id']} (HTTP {status})")
            erro += 1

    print(f"\nDeletados: {ok} | Erros: {erro}")
    if erro:
        sys.exit(1)


if __name__ == "__main__":
    main()
