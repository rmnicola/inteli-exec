#!/usr/bin/env bash
# Gera o PDF A4 de um documento impresso Inteli e as imagens das páginas para revisão.
#
#   design-system/tools/doc.sh <documento.html> [páginas esperadas]
#
# Saídas, ao lado do HTML:
#   <documento>.pdf           o PDF para imprimir
#   qa/<documento>-N.png      uma imagem por página (revise antes de imprimir; não publicar)
# Sai com código 1 se o número de páginas for diferente do esperado.
set -euo pipefail

src=$(realpath "$1")
esperado=${2:-}
dir=$(dirname "$src")
nome=$(basename "$src" .html)
pdf="$dir/$nome.pdf"

perfil=$(mktemp -d "${TMPDIR:-/tmp}/doc-XXXX")
trap 'rm -rf "$perfil"' EXIT
chromium --headless=new --disable-gpu --no-sandbox --user-data-dir="$perfil" \
  --no-pdf-header-footer --virtual-time-budget=5000 \
  --print-to-pdf="$pdf" "file://$src" 2>/dev/null

paginas=$(pdfinfo "$pdf" | awk '/^Pages:/ {print $2}')
mkdir -p "$dir/qa"
rm -f "$dir/qa/$nome"-*.png
pdftoppm -r 80 -png "$pdf" "$dir/qa/$nome"

echo "$pdf ($paginas páginas)"
ls "$dir/qa/$nome"-*.png
if [[ -n "$esperado" && "$paginas" != "$esperado" ]]; then
  echo "erro: esperava $esperado páginas" >&2
  exit 1
fi
