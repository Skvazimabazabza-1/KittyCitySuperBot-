from flask import Flask
from threading import Thread
import time
import requests
import os

app = Flask('')

@app.route('/')
def home():
    return "🐱 Kitty City Bot is running 24/7!"

@app.route('/ping')
def ping():
    return "pong"

@app.route('/health')
def health():
    return "OK"

@app.route('/api/status')
def status():
    return {
        "status": "online",
        "timestamp": time.time(),
        "service": "kitty-bot"
    }

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
    # Дополнительные пинги для надежности
    def background_pinger():
        while True:
            try:
                # Пинг сами себя
                repl_slug = os.getenv('REPL_SLUG', 'KittyCitySuperBot-1')
                repl_owner = os.getenv('REPL_OWNER', 'timabrilevich')
                base_url = f"https://{repl_slug}.{repl_owner}.repl.co"
                
                requests.get(f"{base_url}/", timeout=10)
                requests.get(f"{base_url}/ping", timeout=10)
                requests.get(f"{base_url}/health", timeout=10)
                
                time.sleep(300)  # Пинг каждые 5 минут
            except Exception as e:
                print(f"Background ping error: {e}")
                time.sleep(60)
    
    ping_thread = Thread(target=background_pinger)
    ping_thread.daemon = True
    ping_thread.start()