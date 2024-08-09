from telegram import Update
from telegram.ext import CallbackContext
from config import ADMINS

def kplayer(update: Update, context: CallbackContext) -> None:
    if update.effective_user.id not in ADMINS:
        update.message.reply_text("You do not have permission to remove players.")
        return
    
    if len(context.args) != 1:
        update.message.reply_text("Please provide the username or ID of the player to remove.")
        return
    
    player_id = context.args[0]
    game_data = context.chat_data.get('game')
    
    if not game_data:
        update.message.reply_text("No game is currently active.")
        return
    
    players = game_data['players']
    
    if player_id not in players:
        update.message.reply_text(f"Player {player_id} is not in the game.")
        return
    
    players.remove(player_id)
    update.message.reply_text(f"Player {player_id} has been removed from the game.")
