from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
    buttons = [
        [InlineKeyboardButton("Support", url="https://t.me/grouptdsupport")],
        [InlineKeyboardButton("Feedback", callback_data='feedback')],
        [InlineKeyboardButton("Test Group Chat", url="https://t.me/grouptdtest")],
        [InlineKeyboardButton("Add me to your group", url="https://t.me/your_bot_username?startgroup=true")]
    ]
    return InlineKeyboardMarkup(buttons)

def mode_selection_keyboard():
    buttons = [
        [InlineKeyboardButton("Solo", callback_data='mode_solo')],
        [InlineKeyboardButton("Multiplayer", callback_data='mode_multiplayer')]
    ]
    return InlineKeyboardMarkup(buttons)

def truth_dare_keyboard():
    buttons = [
        [InlineKeyboardButton("Truth", callback_data='truth')],
        [InlineKeyboardButton("Dare", callback_data='dare')]
    ]
    return InlineKeyboardMarkup(buttons)
