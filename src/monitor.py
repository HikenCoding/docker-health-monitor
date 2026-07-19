import docker
import time

# Unser Zustandsspeicher im RAM (Deduplizierung)
# Key: Container-ID, Value: Letzter bekannter Status
ALARMED_CONTAINERS = {}

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
                # Nur alarmieren, wenn wir für diesen Container nicht schon Alarm geschlagen haben
                if c_id not in ALARMED_CONTAINERS:
                    print(f"🚨 NEUER ALARM: Container '{name}' ist offline! Status: [{status.upper()}]")
                    ALARMED_CONTAINERS[c_id] = status
                else:
                    print(f"😴 Spam-Schutz aktiv: '{name}' ist immer noch offline. Kein neuer Alarm.")
            else:
                # Wenn der Container (wieder) läuft, aber vorher defekt war
                if c_id in ALARMED_CONTAINERS:
                    print(f"🎉 ENTWARNUNG: Container '{name}' läuft wieder!")
                    del ALARMED_CONTAINERS[c_id]
                else:
                    print(f"✅ OK: '{name}' läuft.")
                    
        print(f"--- Check beendet. Aktuell im Fehlerspeicher: {len(ALARMED_CONTAINERS)} Container ---\n")
            
    except Exception as e:
        print(f"❌ Fehler beim Health-Check: {e}")

def main():
    CHECK_INTERVAL = 5  # 5 Sekunden für unsere Testphase
    print(f"🚀 Docker-Health-Monitor aktiv. Intervall: {CHECK_INTERVAL}s")
    
    try:
        while True:
            check_container_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Monitor vom Admin beendet. Bis bald!")

if __name__ == "__main__":
    main()