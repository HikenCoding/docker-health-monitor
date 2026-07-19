import docker
import time

def check_container_health():
    print("🔄 Starte Health-Check der Container...")
    try:
        client = docker.from_env()
        containers = client.containers.list(all=True)
        
        unhealthy_count = 0
        for container in containers:
            if container.status != "running":
                print(f"⚠️ ACHTUNG: Container '{container.name}' ist offline! Status: [{container.status.upper()}]")
                unhealthy_count += 1
        
        print(f"--- CHECK BEENDET ({unhealthy_count} Probleme gefunden) ---\n")
            
    except Exception as e:
        print(f"❌ Fehler beim Health-Check: {e}")

def main():
    CHECK_INTERVAL = 5  # Sekunden für die Testphase
    print(f"🚀 Docker-Health-Monitor gestartet. Intervall: {CHECK_INTERVAL}s")
    
    try:
        while True:
            check_container_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Monitor vom Admin beendet. Ciao!")

if __name__ == "__main__":
    main()