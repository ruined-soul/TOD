from telegram import Update
from telegram.ext import CallbackContext

def remove_question(update: Update, context: CallbackContext) -> None:
    question_type = context.args[0].lower() if context.args else None
    question = ' '.join(context.args[1:])
    
    if question_type not in ['truth', 'dare']:
        update.message.reply_text("Specify the question type as either 'truth' or 'dare'.")
        return
    
    if not question:
        update.message.reply_text("Please provide the question to remove.")
        return
    
    if question_type == 'truth':
        questions = context.bot_data.get('truth_questions', [])
    elif question_type == 'dare':
        questions = context.bot_data.get('dare_questions', [])
    
    if question in questions:
        questions.remove(question)
        update.message.reply_text(f"{question_type.capitalize()} question removed: {question}")
    else:
        update.message.reply_text(f"{question_type.capitalize()} question not found.")
