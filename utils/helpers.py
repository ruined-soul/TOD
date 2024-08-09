from telegram import Update
from telegram.ext import CallbackContext
from database.db_manager import DBManager
from models.user import User

def get_or_create_user(update: Update, context: CallbackContext):
    db = context.bot.get_db()
    user_id = update.effective_user.id
    db_manager = DBManager(db)
    
    user = db_manager.get_user(user_id)
    if not user:
        user = User(id=user_id, username=update.effective_user.username)
        db_manager.add_user(user)
    
    return user

def add_question_to_db(update: Update, context: CallbackContext, question_text: str, question_type: str, is_adult: bool = False):
    db = context.bot.get_db()
    db_manager = DBManager(db)
    question = Question(text=question_text, type=question_type, is_adult=is_adult)
    db_manager.add_question(question)
    update.message.reply_text(f"{question_type.capitalize()} question added successfully!")
