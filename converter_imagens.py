"""
Conversor de imagens PNG → WebP
Redimensiona para 1200×628px com crop centralizado e salva em /convertidas
"""

from pathlib import Path
from PIL import Image

PASTA_ORIGEM = Path(r"C:\Users\rhuan\OneDrive\Área de Trabalho\banca")
PASTA_DESTINO = PASTA_ORIGEM / "convertidas"
LARGURA_ALVO = 1200
ALTURA_ALVO = 628
QUALIDADE = 80


def crop_centralizado(img: Image.Image, largura: int, altura: int) -> Image.Image:
    """Recorta a imagem de forma centralizada para atingir a proporção alvo."""
    w, h = img.size
    ratio_alvo = largura / altura
    ratio_original = w / h

    if ratio_original > ratio_alvo:
        # Imagem mais larga que o alvo → corta as laterais
        nova_largura = int(h * ratio_alvo)
        left = (w - nova_largura) // 2
        img = img.crop((left, 0, left + nova_largura, h))
    elif ratio_original < ratio_alvo:
        # Imagem mais alta que o alvo → corta o topo e base
        nova_altura = int(w / ratio_alvo)
        top = (h - nova_altura) // 2
        img = img.crop((0, top, w, top + nova_altura))

    return img.resize((largura, altura), Image.LANCZOS)


def converter():
    if not PASTA_ORIGEM.exists():
        print(f"Pasta não encontrada: {PASTA_ORIGEM}")
        return

    PASTA_DESTINO.mkdir(exist_ok=True)

    arquivos = list(PASTA_ORIGEM.glob("*.png"))
    if not arquivos:
        print("Nenhum arquivo PNG encontrado na pasta.")
        return

    print(f"Encontrados {len(arquivos)} arquivo(s) PNG\n")

    for arquivo in sorted(arquivos):
        destino = PASTA_DESTINO / (arquivo.stem + ".webp")
        try:
            with Image.open(arquivo) as img:
                img = img.convert("RGB")
                img = crop_centralizado(img, LARGURA_ALVO, ALTURA_ALVO)
                img.save(destino, format="WEBP", quality=QUALIDADE, method=6)
            tamanho_kb = destino.stat().st_size // 1024
            print(f"  OK  {arquivo.name} → {destino.name} ({tamanho_kb} KB)")
        except Exception as e:
            print(f"ERRO  {arquivo.name}: {e}")

    print(f"\nConcluído. Arquivos salvos em: {PASTA_DESTINO}")


if __name__ == "__main__":
    converter()
