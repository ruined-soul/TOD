from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
from telegram.ext import InlineQueryHandler

def inline_mode(update, context):
    query = update.inline_query.query.lower()
    
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Truth",
            input_message_content=InputTextMessageContent("/truth"),
            description="Select Truth mode for the game"
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Dare",
            input_message_content=InputTextMessageContent("/dare"),
            description="Select Dare mode for the game"
        ),
    ]
    
    update.inline_query.answer(results)

def setup_inline_mode(dispatcher):
    dispatcher.add_handler(InlineQueryHandler(inline_mode))
