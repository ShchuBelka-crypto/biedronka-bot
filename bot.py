import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

PRODUCT_LIST = [
    "Курица",
    "Индейка",
    "Рис",
    "Гречка",
    "Красная рыба",
    "Молоко безлактозное"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 💛 Я твой Biedronka-бот.\n\n"
        "Команды:\n"
        "/spisok — показать список\n"
        "/akcje — акции (демо)\n"
        "/budzet — бюджет\n"
        "/kiedy_isc — когда идти в магазин"
    )

async def spisok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Твой список продуктов:\n\n"
    for item in PRODUCT_LIST:
        text += f"• {item}\n"
    await update.message.reply_text(text)

async def akcje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Акции недели (демо версия):\n\n"
        "Курица — 8,99 zł\n"
        "Красная рыба — 27,99 zł\n"
        "Рис — без акции"
    )

async def budzet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Бюджет (демо):\n"
        "Потрачено: 0 zł\n"
        "Экономия: 0 zł"
    )

async def kiedy_isc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Лучше идти в четверг — больше всего акций."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spisok", spisok))
    app.add_handler(CommandHandler("akcje", akcje))
    app.add_handler(CommandHandler("budzet", budzet))
    app.add_handler(CommandHandler("kiedy_isc", kiedy_isc))

    app.run_polling()

if __name__ == "__main__":
    main()
