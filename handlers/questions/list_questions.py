from telegram import Update
from telegram.ext import CallbackContext

def list_questions(update: Update, context: CallbackContext) -> None:
    question_type = context.args[0].lower() if context.args else None
    
    if question_type not in ['truth', 'dare']:
        update.message.reply_text("Specify the question type as either 'truth' or 'dare'.")
        return
    
    if question_type == 'truth':
        questions = context.bot_data.get('truth_questions', [])
    elif question_type == 'dare':
        questions = context.bot_data.get('dare_questions', [])
    
    if questions:
        update.message.reply_text(f"Here are the {question_type.capitalize()} questions:\n" + "\n".join(questions))
    else:
        update.message.reply_text(f"No {question_type} questions found.")
