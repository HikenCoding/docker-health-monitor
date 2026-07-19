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


## 🛠️ Technologie-Stack

Dieses Projekt kombiniert moderne DevOps-Werkzeuge, Cloud-Praktiken und Software-Entwicklung nach Industriestandard:

- **Python 3.10:** Die Kern-Programmiersprache für die Logik des Monitors.
- **Docker & Docker-API:** Zur Containerisierung des Tools und für das Auslesen des lokalen Docker-Sockets (`/var/run/docker.sock`).
- **GitHub Actions (CI/CD):** Automatisierte Pipeline zur kontinuierlichen Qualitäts- und Syntaxprüfung bei jedem Code-Push.
- **Git:** Versionsverwaltung mit strukturierter Commit-Historie nach dem *Conventional Commits*-Standard (`feat:`, `sec:`, `docs:`).
- **python-dotenv:** Sicheres Konfigurationsmanagement über Umgebungsvariablen (`.env`), um sensible Daten (Secrets) vom Quellcode zu trennen.
- **Python Requests & Webhooks:** Für die Echtzeit-Kommunikation und das Abfeuern von strukturierten JSON- payloads an externe HTTP-Endpunkte.
- **VirtualBox & Ubuntu Linux:** Die zugrundeliegende, isolierte Entwicklungsumgebung.


Vielen Spaß beim Ausprobieren!