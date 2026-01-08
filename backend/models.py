from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from database import Base

class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True)
    title = Column(String)

class List(Base):
    __tablename__ = "lists"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    position = Column(Integer)
    board_id = Column(Integer, ForeignKey("boards.id"))

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    position = Column(Integer)
    list_id = Column(Integer, ForeignKey("lists.id"))
    due_date = Column(Date, nullable=True)

class ChecklistItem(Base):
    __tablename__ = "checklist_items"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    completed = Column(Boolean, default=False)
    card_id = Column(Integer, ForeignKey("cards.id"))
