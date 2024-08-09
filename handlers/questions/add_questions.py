from telegram import Update
from telegram.ext import CallbackContext

def add_question(update: Update, context: CallbackContext) -> None:
    question_type = context.args[0].lower() if context.args else None
    question = ' '.join(context.args[1:])
    
    if question_type not in ['truth', 'dare']:
        update.message.reply_text("Specify the question type as either 'truth' or 'dare'.")
        return
    
    if not question:
        update.message.reply_text("Please provide a question to add.")
        return
    
    if question_type == 'truth':
        truth_questions = context.bot_data.setdefault('truth_questions', [])
        truth_questions.append(question)
        update.message.reply_text(f"Truth question added: {question}")
    elif question_type == 'dare':
        dare_questions = context.bot_data.setdefault('dare_questions', [])
        dare_questions.append(question)
        update.message.reply_text(f"Dare question added: {question}")
