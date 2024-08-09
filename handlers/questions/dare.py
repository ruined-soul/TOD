from telegram import Update
from telegram.ext import CallbackContext

def add_dare_question(update: Update, context: CallbackContext) -> None:
    question = ' '.join(context.args)
    if not question:
        update.message.reply_text("Please provide a dare question to add.")
        return
    
    dare_questions = context.bot_data.setdefault('dare_questions', [])
    dare_questions.append(question)
    update.message.reply_text(f"Dare question added: {question}")
