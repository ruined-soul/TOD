from telegram import Update, CallbackContext

def feedback_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Please send your feedback here: @ruined_soul or @indiphoenix.")
