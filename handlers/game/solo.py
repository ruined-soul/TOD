from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import random

def solo_mode(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Truth", callback_data='solo_truth'),
            InlineKeyboardButton("Dare", callback_data='solo_dare'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "You chose Solo mode. Select Truth or Dare:",
        reply_markup=reply_markup
    )

def ask_truth_question(update: Update, context: CallbackContext) -> None:
    # Example logic to send a random truth question
    questions = context.bot_data.get('truth_questions', ["What is your biggest fear?", "Have you ever lied to your best friend?"])
    question = random.choice(questions)
    update.message.reply_text(f"Truth: {question}")
    
def ask_dare_question(update: Update, context: CallbackContext) -> None:
    # Example logic to send a random dare
    dares = context.bot_data.get('dare_questions', ["Dance for 30 seconds without music.", "Text your crush and say you like them."])
    dare = random.choice(dares)
    update.message.reply_text(f"Dare: {dare}")
