import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте 👋\n\nОтправьте резюме")

async def handle_doc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Файл получен. Анализирую... 🤖")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, handle_doc))

app.run_polling()
