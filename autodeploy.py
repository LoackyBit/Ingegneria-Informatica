#!/usr/bin/env python3
"""
autodeploy.py - Watcher automatico con debounce per la sincronizzazione e il deploy su GitHub Pages.
Monitora le modifiche alle note di Ingegneria Informatica nel Vault Obsidian e,
dopo 30 secondi di inattività (debounce), esegue deploy.sh.
"""

import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path("/Users/lorenzo/Documents/GitHub/loackyPKM")
TARGET_DIR = Path("/Users/lorenzo/Documents/Ingegneria-Informatica")
DEPLOY_SCRIPT = TARGET_DIR / "deploy.sh"
DEBOUNCE_SECONDS = 30
CHECK_INTERVAL_SECONDS = 4

WATCH_DIRS = [
    VAULT_ROOT / "02 - Atlas/Education & Learning/University/Ingegneria Informatica 2026-27",
    VAULT_ROOT / "99 - Meta/Attachments/Fondamenti di Matematica (Analisi 1)",
    VAULT_ROOT / "99 - Meta/Attachments/Introduzione alla Programmazione",
    VAULT_ROOT / "99 - Meta/Attachments/Probabilità e Statistica",
]

WATCH_FILES = [
    VAULT_ROOT / "01 - Map of Content/Ingegneria Informatica 2026 - 27 MOC.md",
    VAULT_ROOT / "01 - Map of Content/Fondamenti di Matematica (Analisi 1) MOC.md",
    VAULT_ROOT / "01 - Map of Content/Introduzione alla Programmazione MOC.md",
    VAULT_ROOT / "01 - Map of Content/Probabilità e Statistica MOC.md",
]

def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)

def get_snapshot() -> dict[str, tuple[float, int]]:
    """Cattura lo stato di tutti i file monitorati (mtime, dimensione)."""
    snapshot = {}
    
    # Singoli file
    for f in WATCH_FILES:
        if f.exists() and f.is_file():
            try:
                st = f.stat()
                snapshot[str(f)] = (st.st_mtime, st.st_size)
            except OSError:
                pass

    # Directory ricorsive
    for d in WATCH_DIRS:
        if d.exists() and d.is_dir():
            for root, _, files in os.walk(d):
                for file_name in files:
                    if file_name.startswith(".") or file_name.endswith(".DS_Store"):
                        continue
                    full_path = Path(root) / file_name
                    try:
                        st = full_path.stat()
                        snapshot[str(full_path)] = (st.st_mtime, st.st_size)
                    except OSError:
                        pass

    return snapshot

def run_deploy():
    """Esegue il deploy script."""
    log("🚀 Avvio deploy automatico su GitHub Pages...")
    try:
        res = subprocess.run(
            [str(DEPLOY_SCRIPT)],
            cwd=str(TARGET_DIR),
            capture_output=True,
            text=True,
            timeout=180,
        )
        if res.returncode == 0:
            log("✅ Deploy completato con successo:\n" + res.stdout.strip())
        else:
            log(f"⚠️ Errore durante il deploy (code {res.returncode}):\n{res.stderr.strip()}")
    except Exception as e:
        log(f"❌ Eccezione durante l'esecuzione del deploy: {e}")

def main():
    log(f"👀 Avviato monitoraggio per Ingegneria Informatica (debounce: {DEBOUNCE_SECONDS}s)...")
    last_state = get_snapshot()
    pending = False
    last_change_time = 0.0

    while True:
        try:
            time.sleep(CHECK_INTERVAL_SECONDS)
            current_state = get_snapshot()

            if current_state != last_state:
                # Modifica rilevata
                now = time.time()
                last_change_time = now
                pending = True
                last_state = current_state
                log(f"📝 Rilevata modifica alle note. Attesa debounce di {DEBOUNCE_SECONDS}s di inattività...")

            if pending and (time.time() - last_change_time >= DEBOUNCE_SECONDS):
                run_deploy()
                pending = False
                last_state = get_snapshot()

        except KeyboardInterrupt:
            log("🛑 Arresto manuale del demone.")
            sys.exit(0)
        except Exception as e:
            log(f"⚠️ Errore nel loop di monitoraggio: {e}")
            time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
