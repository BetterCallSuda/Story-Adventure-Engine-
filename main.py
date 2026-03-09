from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# -----------------------------
# DATABASE SETUP
# -----------------------------

engine = create_engine("sqlite:///story_game.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# -----------------------------
# DATABASE MODELS
# -----------------------------

class Player(Base):

    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)


class ChoiceHistory(Base):

    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    location = Column(String)
    decision = Column(String)


Base.metadata.create_all(engine)

