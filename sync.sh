#!/bin/bash
set -e

REPO_DIR="/Users/lorenzo/Documents/Ingegneria-Informatica"
VAULT_DIR="/Users/lorenzo/Documents/GitHub/loackyPKM"
CONTENT_DIR="$REPO_DIR/content"

echo "🔄 Sincronizzazione appunti da loackyPKM a Ingegneria-Informatica..."

# Pulizia cartella content (mantenendo solo la struttura)
rm -rf "$CONTENT_DIR"
mkdir -p "$CONTENT_DIR"
mkdir -p "$CONTENT_DIR/attachments"

# 1. Copia cartella principale corsi
cp -R "$VAULT_DIR/02 - Atlas/Education & Learning/University/Ingegneria Informatica 2026-27/"* "$CONTENT_DIR/"

# 2. Copia i singoli Course MOC nelle rispettive cartelle
cp "$VAULT_DIR/01 - Map of Content/Fondamenti di Matematica (Analisi 1) MOC.md" "$CONTENT_DIR/Fondamenti di Matematica (Analisi 1)/"
cp "$VAULT_DIR/01 - Map of Content/Introduzione alla Programmazione MOC.md" "$CONTENT_DIR/Introduzione alla Programmazione/"
cp "$VAULT_DIR/01 - Map of Content/Probabilità e Statistica MOC.md" "$CONTENT_DIR/Probabilità e Statistica/"

# 3. Copia Master Hub come index.md (Home del sito)
cp "$VAULT_DIR/01 - Map of Content/Ingegneria Informatica 2026 - 27 MOC.md" "$CONTENT_DIR/index.md"
sed -i '' 's/title: "Ingegneria Informatica 2026 - 27 MOC"/title: "Ingegneria Informatica 2026\/27"/' "$CONTENT_DIR/index.md"

# 4. Copia tutti gli schemi e grafici (immagini) in attachments
find "$VAULT_DIR/99 - Meta/Attachments" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" \) -exec cp {} "$CONTENT_DIR/attachments/" \;

# Rimuovi file .DS_Store se presenti
find "$CONTENT_DIR" -name ".DS_Store" -delete

echo "✅ Sincronizzazione completata con successo in $CONTENT_DIR"
