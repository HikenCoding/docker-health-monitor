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


## 🧪 So können Recruiter / Entwickler das Projekt testen

Das Projekt ist vollständig dockerisiert. Das bedeutet, Sie müssen **kein Python** oder zusätzliche Bibliotheken auf Ihrem System installieren. Sie benötigen lediglich eine installierte Docker-Umgebung.

### Schritt-für-Schritt-Anleitung:

1. **Repository klonen & Verzeichnis wechseln:**
   ```bash
   git clone <HIER_DEIN_GITHUB_REPO_LINK_EINFÜGEN>
   cd docker-health-monitor
    ```

2. **Webhook-URL vorbereiten:**
- Gehen Sie auf **Webhook.site** und kopieren Sie Ihre einzigartige Test-URL.
- Kopieren Sie die Datei `.env.example` und nennen Sie sie `.env`:
    ```bash
   cp .env.example .env
    ```
- Öffnen Sie die `.env` und fügen Sie Ihre URL ein (wichtig: ohne Leerzeichen um das `=`):
    ```bash
   WEBHOOK_URL="[https://webhook.site/ihre-id](https://webhook.site/ihre-id)"
    ```

3. **Das Docker-Image lokal bauen:**
    ```bash
   docker build -t docker-health-monitor:latest .
    ```

4. **Den Monitor als Container starten (mit Docker-Socket-Anbindung):**
    ```bash
    docker run -d --name docker-health-monitor -v /var/run/docker.sock:/var/run/docker.sock --env-file .env docker-health-monitor:latest
    ```

5. **Ergebnis prüfen:**
Schauen Sie nun in Ihren geöffneten Browser-Tab von Webhook.site. Dort kommen nun live die Alarme an, die der Container vollautomatisch aus Ihrer Umgebung sendet!


## 🚀 Manueller Schnellstart (Alternativ ohne Docker-Container)

Falls Sie das Skript lieber direkt lokal in einer virtuellen Python-Umgebung ausführen möchten:

1. Virtuelle Umgebung einrichten und aktivieren:
    ```bash
   python -m venv .venv
source .venv/bin/activate
    ```

2. Abhängigkeiten installieren:
    ```bash
   pip install -r requirements.txt
    ```

3.  `.env`-Datei wie oben beschrieben anlegen.

4. Skript starten:
    ```bash
   python src/monitor.py
    ```


Vielen Spaß beim Ausprobieren!


## ✍🏽 Persönliche Zusammenfassung Erklärung dieses Projektes 
**Was genau macht das Projekt den eigentlich?**
Es ist praktisch eine automatische Alarmanlage. Wir können uns das so vorstellen:
Der Monitor schaut durch das Schlüsselloch (den Docker-Socket)
Dann sieht er sofort, wenn ein Container abstürzt oder neu startet
Und als nächstes, falls etwas passiert, schickt er sofort eine SMS/Nachricht an dich (das sieht man im Webhook)

Es gibt insgesamt vier wichtige Bausteine 🟦:
1. Der Draht zum Docker (Schnittstelle, welches direkt mit der Docker-Zentrale des Computers spricht. Weiß in Echtzeit, was mit allen Containern passiert)
2. Nachrichten Funktion (HTTP-POST-Webhook) (Status eines Containers ändert sich, Python packt kleine Info Nachricht JSON zusammen, sendet per Internet an Ziel URL im Webhook)
3. Spam-Schutz (Container schwankt kurz hintereinander und man will nicht 200 Nachrichten pro Minuten bekommen. Skript merkt sich RAM und letzten Status und sendet nur 1 Nachricht, wenn Zustand sich wirklich ändert) Somit keinen Spam. Deswegen Spam-Schutz ;-)
4. Sichere Konfiguration (.env) Passwörter oder Webhook-Urls stehen nicht fest im Code, sondern in seperaten Textdateien (.env). Code kann sicher auf Github hochgeladen werden.

 **Was genau ist den der Webhook?**
 Es ist wie eine automatische Push Benachrichtung. Wenn man eine Pizza bestellt (hmm lecker hab gerade voll Lust auf eine) dann gibt man seine Hindernummer an. Man wird nicht alle 2 Minuten benachrichtigt, was jetzt ist. Hat der Pizzabäcker den teig gut geknetet? Hat er sich die Hände gewaschen? Ist die Pizza im Ofen. Das wären zu viele Infos und würden uns nur nerven. Stattdessen bekommt man eine SMS, sobald der Fahrer unterwegs ist. Und das ist quasi der Webhook. Die SMS in dem Fall ist der Webhook.

 **Warum dieses Projekt?**
 Mit dem Projekt, wollte ich in die Aufgabenbereich eines IT-Systemadministrator eintauchen, weil ich mich als Softwareentwickler nicht nur die Softwareentwickklung interessiere, sondern auch was alles dahinter genau passiert und auch um das Netzwerk-Thema. Ich finde es sehr interessant und habe auch deswegen auch weitere Projekte zum Thema Netzwerk / Infrastruktur realisiert.


