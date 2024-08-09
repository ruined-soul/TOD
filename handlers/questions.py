from telegram import Update, CallbackContext

def add_truth_question(update: Update, context: CallbackContext) -> None:
    # Logic to add a truth question
    update.message.reply_text("Truth question added.")

def add_dare_question(update: Update, context: CallbackContext) -> None:
    # Logic to add a dare question
    update.message.reply_text("Dare question added.")

def add_penalty(update: Update, context: CallbackContext) -> None:
    # Logic to add a penalty
    update.message.reply_text("Penalty added.")

def list_questions(update: Update, context: CallbackContext) -> None:
    # Logic to list all questions
    update.message.reply_text("List of all questions: ...")

def remove_question(update: Update, context: CallbackContext) -> None:
    # Logic to remove a question
    update.message.reply_text("Question removed.")
