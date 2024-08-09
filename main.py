# main.py

import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from config import (
    BOT_TOKEN,
    FIRST_BOT_OWNER_ID,
    SECOND_BOT_OWNER_ID,
    SUPPORT_CHAT_INVITE_LINK,
    TEST_GROUP_CHAT_INVITE_LINK,
    ALIVE_COMMAND,
    START_COMMAND,
    HELP_COMMAND,
    FEEDBACK_COMMAND,
    ADD_TRUTH_COMMAND,
    ADD_DARE_COMMAND,
    ADD_PENALTY_COMMAND,
    LIST_QUESTIONS_COMMAND,
    REMOVE_QUESTION_COMMAND,
    KICK_PLAYER_COMMAND,
    BROADCAST_COMMAND,
    STATS_COMMAND,
    LISGC_COMMAND,
    SOLO_MODE,
    MULTIPLAYER_MODE,
    TRUTH_QUESTIONS,
    DARE_QUESTIONS,
    PENALTIES,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command Handlers
async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    user = update.effective_user
    buttons = [
        [
            InlineKeyboardButton("Support", url=SUPPORT_CHAT_INVITE_LINK),
            InlineKeyboardButton("Test Group", url=TEST_GROUP_CHAT_INVITE_LINK),
        ],
        [
            InlineKeyboardButton("Feedback", callback_data="feedback"),
            InlineKeyboardButton("Add me to your group", url=f"http://t.me/{context.bot.username}?startgroup=true"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        f"✨ Welcome {user.first_name}! ✨\n\n"
        "I am a Truth and Dare bot with multiple features to make your game more exciting!\n\n"
        "Use the buttons below to navigate through the bot.",
        reply_markup=reply_markup,
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    """Handle the /help command."""
    buttons = [
        [InlineKeyboardButton("Alive", callback_data="help_alive")],
        [InlineKeyboardButton("Start", callback_data="help_start")],
        [InlineKeyboardButton("Feedback", callback_data="help_feedback")],
        [InlineKeyboardButton("Truth Questions", callback_data="help_addtruth")],
        [InlineKeyboardButton("Dare Questions", callback_data="help_adddare")],
        [InlineKeyboardButton("Penalties", callback_data="help_addpenalty")],
        # Add more buttons for other commands as needed
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "🛠 Bot Commands:\n\nSelect a command to see its details.",
        reply_markup=reply_markup,
    )

async def alive(update: Update, context: CallbackContext) -> None:
    """Handle the /alive command."""
    await update.message.reply_text("✅ I'm alive and ready to play!")

async def feedback(update: Update, context: CallbackContext) -> None:
    """Handle the /feedback command."""
    user = update.effective_user
    feedback_message = " ".join(context.args)
    if feedback_message:
        # Send the feedback to bot owner(s)
        feedback_text = f"📬 Feedback from {user.first_name} (@{user.username}):\n\n{feedback_message}"
        await context.bot.send_message(chat_id=FIRST_BOT_OWNER_ID, text=feedback_text)
        await context.bot.send_message(chat_id=SECOND_BOT_OWNER_ID, text=feedback_text)
        await update.message.reply_text("Thank you for your feedback! 😊")
    else:
        await update.message.reply_text("Please provide your feedback after the command.")

async def button(update: Update, context: CallbackContext) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == "feedback":
        await feedback(update, context)
    elif data.startswith("help_"):
        # Handle the help command details
        command_name = data.split("_", 1)[1]
        command_texts = {
            "alive": "The /alive command checks if the bot is running and functional.",
            "start": "The /start command initiates the bot and provides a welcome message.",
            "feedback": "The /feedback command allows users to send feedback to the developer.",
            "addtruth": "The /addtruth command adds a truth question to the database.",
            "adddare": "The /adddare command adds a dare to the database.",
            "addpenalty": "The /addpenalty command adds a penalty to the database.",
            # Add more details for other commands
        }
        await query.message.edit_text(command_texts.get(command_name, "Command details not found."))

# Other command handlers (addtruth, adddare, etc.) can be implemented similarly

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler(START_COMMAND.strip('/'), start))
    application.add_handler(CommandHandler(HELP_COMMAND.strip('/'), help_command))
    application.add_handler(CommandHandler(ALIVE_COMMAND.strip('/'), alive))
    application.add_handler(CommandHandler(FEEDBACK_COMMAND.strip('/'), feedback))
    application.add_handler(CallbackQueryHandler(button))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
