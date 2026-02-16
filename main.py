import os
import threading
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Запускаем веб-сервер в отдельном потоке
threading.Thread(target=run_web).start()

# ⬇️ Здесь твой запуск бота
bot.polling(none_stop=True)