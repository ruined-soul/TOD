from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def multiplayer_mode(update: Update, context: CallbackContext) -> None:
    context.chat_data['players'] = []
    keyboard = [
        [InlineKeyboardButton("Join Game", callback_data='join_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "You chose Multiplayer mode. Click the button below to join the game:",
        reply_markup=reply_markup
    )

def handle_join_game(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    players = context.chat_data.get('players', [])
    
    if user.id not in [p['id'] for p in players]:
        players.append({"id": user.id, "username": user.username})
        context.chat_data['players'] = players
        update.callback_query.answer(f"{user.username} has joined the game!")
    else:
        update.callback_query.answer(f"{user.username}, you have already joined the game.")

    if len(players) >= 2:
        update.callback_query.message.reply_text("Enough players have joined. Starting the game...")
        start_game(context)
    else:
        update.callback_query.message.reply_text(f"{len(players)} players joined. Waiting for more...")

def start_game(context: CallbackContext) -> None:
    players = context.chat_data['players']
    context.chat_data['current_player_index'] = 0
    ask_next_player(context)

def ask_next_player(context: CallbackContext) -> None:
    players = context.chat_data['players']
    current_player_index = context.chat_data.get('current_player_index', 0)
    current_player = players[current_player_index]

    keyboard = [
        [
            InlineKeyboardButton("Truth", callback_data='multiplayer_truth'),
            InlineKeyboardButton("Dare", callback_data='multiplayer_dare'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=current_player['id'],
        text=f"Your turn, {current_player['username']}! Choose Truth or Dare:",
        reply_markup=reply_markup
    )

    # Advance to the next player after the current player's turn
    context.chat_data['current_player_index'] = (current_player_index + 1) % len(players)
