from telegram import Update
from telegram.ext import CallbackContext
from config import ADMINS

def change_mode(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id not in ADMINS:
        update.message.reply_text("You do not have permission to change the game mode.")
        return
    
    if len(context.args) != 1 or context.args[0].lower() not in ['solo', 'multiplayer']:
        update.message.reply_text("Please specify the mode as 'solo' or 'multiplayer'.")
        return
    
    mode = context.args[0].lower()
    context.chat_data['game_mode'] = mode
    update.message.reply_text(f"Game mode changed to: {mode.capitalize()}")
