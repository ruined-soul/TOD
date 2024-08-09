from functools import wraps
from telegram import Update
from telegram.ext import CallbackContext

def restricted(func):
    @wraps(func)
    def wrapped(update: Update, context: CallbackContext, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in [1159381624, 7329859398]:  # Owner IDs
            update.message.reply_text("You don't have permission to use this command.")
            return
        return func(update, context, *args, **kwargs)
    return wrapped

def log_errors(func):
    @wraps(func)
    def wrapped(update: Update, context: CallbackContext, *args, **kwargs):
        try:
            return func(update, context, *args, **kwargs)
        except Exception as e:
            update.message.reply_text("An error occurred. Please try again.")
            context.bot.logger.error(f"Error in {func.__name__}: {e}")
            raise e
    return wrapped
