from telegram import Update, CallbackContext

def end_game_command(update: Update, context: CallbackContext) -> None:
    # Logic to end the current game
    update.message.reply_text("The game has been ended by the admin.")
