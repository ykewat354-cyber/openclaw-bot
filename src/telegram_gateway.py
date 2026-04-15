import os, asyncio, logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from core import OpenClawCore
from hybrid_brain import hybrid_chat
load_dotenv()
logging.basicConfig(level=logging.INFO)
class OpenClawBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.agent = OpenClawCore()
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Namaste bhai! 🙏 OpenClaw-Bot Ultra is LIVE! ⚡")
    async def handle_msg(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, hybrid_chat, self.agent, text)
        await update.message.reply_text(response)
    def run(self):
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.handle_msg))
        app.run_polling()
if __name__ == "__main__":
    OpenClawBot().run()
