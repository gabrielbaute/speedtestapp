import threading, time
from app import create_app
from core.testing import save_results

app=create_app()

def background_task():
    while True:
        save_results()
        time.sleep(600)  # Espera 10 minutos

if __name__ == "__main__":
    threading.Thread(target=background_task, daemon=True).start()
    app.run(debug=False, port=5505)