from sqlalchemy import Column, Integer, String, Boolean, Text
from models import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)  # 'truth', 'dare', or 'penalty'
    text = Column(Text, nullable=False)
    is_adult = Column(Boolean, default=False)  # True for 18+ questions

    def __repr__(self):
        return f"<Question(id={self.id}, type={self.type}, is_adult={self.is_adult})>"
