from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# -----------------------------
# DATABASE SETUP
# -----------------------------

engine = create_engine("sqlite:///story_game.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

