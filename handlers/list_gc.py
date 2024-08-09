from telegram import Update, CallbackContext

def list_gc_command(update: Update, context: CallbackContext) -> None:
    # Logic to list all groups where the bot is added
    update.message.reply_text("List of groups the bot is in: ...")
