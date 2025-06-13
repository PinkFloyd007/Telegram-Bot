import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я GPT‑бот. Напиши мне что угодно — я отвечу.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.text
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user}]
    )
    answer = resp.choices[0].message.content.strip()
    await update.message.reply_text(answer)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()
