import os
import docker
import time
import requests
from dotenv import load_dotenv

# Lädt die Variablen aus der .env-Datei in die Umgebungsvariablen des Systems
load_dotenv()

# Hier holen wir uns die URL sicher aus dem System. 
# Falls sie fehlt, brechen wir mit einer klaren Fehlermeldung ab!
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("❌ Kritischer Fehler: WEBHOOK_URL wurde in der .env-Datei nicht gefunden!")

ALARMED_CONTAINERS = {}

def send_webhook_alert(container_name, status, event_type="alarm"):
    """Sendet eine strukturierte JSON-Payload an den konfigurierten Webhook."""
    payload = {
        "event": "Docker Environment Alert",
        "type": event_type,
        "container_name": container_name,
        "status": status.upper(),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code in [200, 201]:
            print(f"📡 Webhook erfolgreich gesendet für '{container_name}' ({event_type})")
        else:
            print(f"❌ Webhook-Fehler: Server antwortete mit Status {response.status_code}")
    except Exception as e:
        print(f"❌ Netzwerkfehler beim Senden des Webhooks: {e}")

def check_container_health():
    print("🔄 Starte Health-Check der Container...")
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)
        
        for container in containers:
            status = container.status
            name = container.name
            c_id = container.id

            if status != "running":
                if c_id not in ALARMED_CONTAINERS:
                    print(f"🚨 NEUER ALARM: Container '{name}' ist offline!")
                    ALARMED_CONTAINERS[c_id] = status
                    send_webhook_alert(name, status, event_type="alarm")
                else:
                    print(f"😴 Spam-Schutz aktiv für '{name}'.")
            else:
                if c_id in ALARMED_CONTAINERS:
                    print(f"🎉 ENTWARNUNG: Container '{name}' läuft wieder!")
                    del ALARMED_CONTAINERS[c_id]
                    send_webhook_alert(name, status, event_type="recovery")
                    
        print(f"--- Check beendet. Fehler-Zustand: {len(ALARMED_CONTAINERS)} ---\n")
            
    except Exception as e:
        print(f"❌ Fehler beim Health-Check: {e}")

def main():
    CHECK_INTERVAL = 5
    print(f"🚀 Docker-Health-Monitor aktiv. Intervall: {CHECK_INTERVAL}s")
    
    try:
        while True:
            check_container_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Monitor beendet. Ciao!")

if __name__ == "__main__":
    main()