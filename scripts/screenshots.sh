#!/usr/bin/env bash
# Quire screenshot script — capture first page/screen of each output as PNG.
# Re-run after rebuilding assets/output/*.html to refresh the thumbnails
# referenced by README.md and index.html.
#
# Usage:
#   ./scripts/screenshots.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/assets/output/screenshots"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$OUT"

# Locate Chrome / Chromium / Edge (same lookup order as build.sh)
CHROME=""
for candidate in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
  "$(command -v google-chrome 2>/dev/null || true)" \
  "$(command -v chromium 2>/dev/null || true)" \
  "$(command -v chrome 2>/dev/null || true)"; do
  if [[ -n "$candidate" && -x "$candidate" ]]; then
    CHROME="$candidate"
    break
  fi
done

if [[ -z "$CHROME" ]]; then
  echo "ERROR: no Chrome / Chromium / Edge found." >&2
  exit 1
fi

# Strip on-screen chrome (view-pdf button, slide hint/counter, body gray
# matting) so the capture matches the printed look.
inject_overrides() {
  local src=$1 dst=$2
  python3 - "$src" "$dst" <<'PY'
import sys
src, dst = sys.argv[1], sys.argv[2]
html = open(src).read()
override = """
<style id="screenshot-overrides">
  .view-pdf, .hint, .counter, .progress { display: none !important; }
  html, body { background: var(--canvas, #f7fbff) !important; }
  .page { margin: 0 !important; outline: none !important; box-shadow: none !important; }
</style>
"""
html = html.replace('</head>', override + '</head>')
open(dst, 'w').write(html)
PY
}

shot() {
  local name=$1 w=$2 h=$3
  local src="$ROOT/assets/output/$name.html"
  local tmp="$TMP/$name.html"
  if [[ ! -f "$src" ]]; then
    echo "skip $name (no $src)"
    return
  fi
  inject_overrides "$src" "$tmp"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 \
    --window-size=$w,$h \
    --screenshot="$OUT/$name.png" \
    --virtual-time-budget=8000 \
    "file://$tmp" 2>/dev/null
  echo "✓ $OUT/$name.png"
}

# viewport in CSS px; 2x device-scale-factor produces retina output
shot quire-white-paper   794 1123    # A4 portrait
shot quire-single-page   794 1123    # A4 portrait
shot quire-landing-page  794 1123    # A4 width, first screen
shot quire-playbook     1056  816    # 11×8.5in landscape
shot quire-slides       1280  720    # 16:9 deck
