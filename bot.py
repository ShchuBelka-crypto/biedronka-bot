import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Получаем токен из Railway Variables
TOKEN = os.environ.get("BOT_TOKEN")

# ===== КОМАНДЫ =====

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋\n\n"
        "Я бот Biedronka.\n"
        "Используй команды:\n"
        "/spisok\n"
        "/akcje\n"
        "/budzet"
    )

async def spisok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    product_list = ["Молоко", "Хлеб", "Яйца"]
    text = "🛒 Твой список продуктов:\n\n"
    for item in product_list:
        text += f"• {item}\n"

    await update.message.reply_text(text)

async def akcje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Акции недели (демо):\n\n"
        "Курица — 8,99 zł\n"
        "Красная рыба — 27,99 zł\n"
        "Рис — без акции"
    )

async def budzet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Бюджет (демо):\n\n"
        "Потрачено: 0 zł\n"
        "Экономия: 0 zł"
    )

# ===== ЗАПУСК =====

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spisok", spisok))
    app.add_handler(CommandHandler("akcje", akcje))
    app.add_handler(CommandHandler("budzet", budzet))

    app.run_polling()

if __name__ == "__main__":
    main()

