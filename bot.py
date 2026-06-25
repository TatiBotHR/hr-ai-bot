import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

from ai import analyze_text
from parser import read_pdf, read_docx

TOKEN = os.getenv("TELEGRAM_TOKEN")


def extract_text(file_path: str):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    return ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Отправьте резюме в формате PDF или DOCX"
    )


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    file = await document.get_file()

    file_name = document.file_name
    file_path = f"resume_{update.message.from_user.id}_{file_name}"

    await file.download_to_drive(file_path)

    text = extract_text(file_path)

    if not text.strip():
        await update.message.reply_text("❌ Не удалось прочитать файл")
        return

    result = analyze_text(text)

    await update.message.reply_text(result)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

app.run_polling()
