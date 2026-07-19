# 1. Wir nutzen ein offizielles, minimales Python-Image
FROM python:3.10-slim

# 2. Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# 3. Kopiere die requirements.txt zuerst (Nutzt Docker-Caching für schnellere Builds!)
COPY requirements.txt .

# 4. Installiere die Python-Abhängigkeiten ohne Cache (spart Platz)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiere den restlichen Quellcode in den Container
COPY src/ ./src/

# 6. Befehl, der ausgeführt wird, wenn der Container startet
CMD ["python", "src/monitor.py"]