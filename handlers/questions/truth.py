from telegram import Update
from telegram.ext import CallbackContext

def add_truth_question(update: Update, context: CallbackContext) -> None:
    question = ' '.join(context.args)
    if not question:
        update.message.reply_text("Please provide a truth question to add.")
        return
    
    truth_questions = context.bot_data.setdefault('truth_questions', [])
    truth_questions.append(question)
    update.message.reply_text(f"Truth question added: {question}")
