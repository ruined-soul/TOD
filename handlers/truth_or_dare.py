from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def handle_truth_or_dare(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Solo", callback_data='solo_mode'),
            InlineKeyboardButton("Multiplayer", callback_data='multiplayer_mode'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "Choose your game mode:",
        reply_markup=reply_markup
    )
