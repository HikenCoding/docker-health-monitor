# 🐳 Docker Health Monitor

Dieses Projekt ist ein automatisierter Health-Monitor für Docker-Umgebungen, geschrieben in Python. Das Tool überwacht den Status aller lokalen Container und sendet bei Ausfällen oder Wiederinbetriebnahmen Echtzeit-Alarme via HTTP-POST-Webhooks.

## ✨ Features
- **Echtzeit-Überwachung:** Direkte Anbindung an den lokalen Docker-Socket.
- **Intelligenter Spam-Schutz:** RAM-basierte Deduplizierung verhindert doppelte Alarmierungen.
- **Sicherheits-Fokus:** Konfiguration und Secrets werden sicher über eine `.env`-Datei geladen.
- **CI/CD Ready:** Automatische Syntax- und Qualitätsprüfung via GitHub Actions bei jedem Push.
- **Fully Containerized:** Kann als autarker Container gestartet werden und überwacht seine "Geschwister".

## 🚀 Schnellstart (Lokal)

1. Repository klonen und in den Ordner wechseln.
2. `.env.example` kopieren zu `.env` und die eigene `WEBHOOK_URL` eintragen.
3. Virtuelle Umgebung einrichten und starten:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

Vielen Spaß beim Ausprobieren!