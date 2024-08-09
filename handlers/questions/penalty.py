from telegram import Update
from telegram.ext import CallbackContext

def add_penalty_question(update: Update, context: CallbackContext) -> None:
    penalty = ' '.join(context.args)
    if not penalty:
        update.message.reply_text("Please provide a penalty to add.")
        return
    
    penalties = context.bot_data.setdefault('penalties', [])
    penalties.append(penalty)
    update.message.reply_text(f"Penalty added: {penalty}")
