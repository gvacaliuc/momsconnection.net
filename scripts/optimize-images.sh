#!/usr/bin/env bash
set -euo pipefail

input_dir="${1:-design/v2}"
output_dir="${2:-design/v2/optimized}"
max_dim="${3:-2000}"
quality="${4:-82}"

if [[ ! -d "$input_dir" ]]; then
  echo "Input directory not found: $input_dir" >&2
  exit 1
fi

mkdir -p "$output_dir"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing dependency: $1" >&2
    exit 1
  }
}

process_with_magick() {
  local file="$1"
  local base ext name out
  base="$(basename "$file")"
  ext="${base##*.}"
  name="${base%.*}"
  ext="$(echo "$ext" | tr '[:upper:]' '[:lower:]')"
  out="$output_dir/$name.$ext"

  if [[ "$ext" == "png" ]]; then
    magick "$file" -strip -resize "${max_dim}x${max_dim}>" \
      -define png:compression-level=9 "$out"
  else
    magick "$file" -strip -resize "${max_dim}x${max_dim}>" \
      -quality "$quality" "$out"
  fi
}

require_cmd magick

shopt -s nullglob
images=("$input_dir"/*.{jpg,JPG,jpeg,JPEG,png,PNG})
if [[ ${#images[@]} -eq 0 ]]; then
  echo "No images found in $input_dir" >&2
  exit 1
fi

for img in "${images[@]}"; do
  process_with_magick "$img"
done

echo "Optimized images written to: $output_dir"
