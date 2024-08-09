from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, index=True)
    mode = Column(String, default="solo")
    active = Column(Boolean, default=True)

    players = relationship("GamePlayer", back_populates="game")

class GamePlayer(Base):
    __tablename__ = "game_players"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)

    game = relationship("Game", back_populates="players")
    user = relationship("User")

    def __repr__(self):
        return f"<GamePlayer(id={self.id}, user_id={self.user_id}, is_active={self.is_active})>"
