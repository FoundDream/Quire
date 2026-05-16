#!/usr/bin/env bash
# Quire build script — HTML → PDF via headless Chrome.
#
# Usage:
#   ./scripts/build.sh                                    # build playbook.html
#   ./scripts/build.sh assets/templates/playbook.html
#   ./scripts/build.sh path/to/your.html out.pdf

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

INPUT="${1:-$ROOT/assets/templates/playbook.html}"
OUTPUT="${2:-${INPUT%.html}.pdf}"

if [[ ! -f "$INPUT" ]]; then
  echo "ERROR: input not found: $INPUT" >&2
  exit 1
fi

# Locate Chrome / Chromium / Edge
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
  echo "ERROR: no Chrome / Chromium / Edge found in PATH or default locations." >&2
  echo "Install Google Chrome or set CHROME env var to the binary path." >&2
  exit 1
fi

echo "Chrome: $CHROME"
echo "Input:  $INPUT"
echo "Output: $OUTPUT"
echo

# Convert input path to absolute file:// URL
ABS_INPUT="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$OUTPUT" \
  --virtual-time-budget=10000 \
  "file://$ABS_INPUT"

echo
echo "✓ Built: $OUTPUT"

# Verify if pdffonts / pdfinfo are available
if command -v pdffonts >/dev/null 2>&1; then
  echo
  echo "Embedded fonts:"
  pdffonts "$OUTPUT" | head -20
fi

if command -v pdfinfo >/dev/null 2>&1; then
  echo
  pdfinfo "$OUTPUT" | grep -E "Pages|Page size"
fi
