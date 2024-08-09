from telegram import Update, CallbackContext

def alive_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅ Bot is alive and working!")
