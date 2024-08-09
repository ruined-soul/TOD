from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Truth/Dare Game", callback_data='truth_or_dare')],
        [InlineKeyboardButton("Add Questions", callback_data='add_questions')],
        [InlineKeyboardButton("Manage Players", callback_data='manage_players')],
        [InlineKeyboardButton("Bot Admin Commands", callback_data='admin_commands')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "💡 Use the buttons below to get more information about commands.",
        reply_markup=reply_markup
    )
