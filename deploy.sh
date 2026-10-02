#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Esegui sincronizzazione delle note e degli schemi da loackyPKM
"$DIR/sync.sh"

cd "$DIR"
git add .

if git diff-index --quiet HEAD --; then
  echo "✨ Nessuna nuova modifica da pubblicare."
else
  git commit -m "chore: sync appunti $(date +'%Y-%m-%d %H:%M')"
  git push origin v4
  echo "🚀 Modifiche inviate a GitHub Pages! Il sito si aggiornerà tra circa 1 minuto."
fi
