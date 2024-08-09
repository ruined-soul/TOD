from sqlalchemy.orm import Session
from models.user import User
from models.game import Game, GamePlayer
from models.question import Question

class DBManager:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_active_game(self, chat_id: int):
        return self.db.query(Game).filter(Game.chat_id == chat_id, Game.active == True).first()

    def add_game(self, game: Game):
        self.db.add(game)
        self.db.commit()
        self.db.refresh(game)
        return game

    def add_question(self, question: Question):
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question

    def list_questions(self, question_type: str, is_adult: bool = False):
        return self.db.query(Question).filter(Question.type == question_type, Question.is_adult == is_adult).all()

    def remove_question(self, question_id: int):
        question = self.db.query(Question).filter(Question.id == question_id).first()
        if question:
            self.db.delete(question)
            self.db.commit()
