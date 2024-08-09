from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Support", url="https://t.me/grouptdsupport"),
            InlineKeyboardButton("Feedback", callback_data='feedback'),
        ],
        [
            InlineKeyboardButton("Test Group", url="https://t.me/grouptdtest"),
            InlineKeyboardButton("Add Me To Your Group", url="https://t.me/YourBot?startgroup=true"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "👋 Welcome to the Truth and Dare Game Bot!\n\n"
        "Use /help to see available commands.\n"
        "Choose an option below to get started:",
        reply_markup=reply_markup
    )
