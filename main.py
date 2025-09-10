from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from wakeonlan import send_magic_packet
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PC_MAC = os.environ.get("PC_MAC", "")
ALLOWED_USER_IDS = os.environ.get("ALLOWED_USER_IDS", "").split(",")


async def wake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id not in ALLOWED_USER_IDS:
        await update.message.reply_text("⛔ У вас нет доступа к этой команде.")
        return

    send_magic_packet(PC_MAC)
    await update.message.reply_text("🔌 Magic Packet sent! ПК должен включиться.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("wake", wake))

print("🚀 Бот запущен...")
app.run_polling()
