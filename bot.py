import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "AAFeD6Ye5FMNTiBZNDDHZErk25EeMMRj9Os"

# simple memory
memory = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Agent ready! Kuch bhi pucho.")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.text

    # save memory
    memory["last"] = user

    # AI response (free API example)
    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer YOUR_API_KEY"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": user}]
            }
        )
        reply = res.json()["choices"][0]["message"]["content"]
    except:
        reply = "⚠️ AI error, check API key"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
