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

# -----------------------------
# STORY DATA
# -----------------------------

story = {

"START": {
"text": "You wake up in a mysterious forest.",
"choices": {
"1": ("Go north toward mountains", "MOUNTAIN"),
"2": ("Go south toward river", "RIVER")
}
},

"MOUNTAIN": {
"text": "You see a dark cave in the mountain.",
"choices": {
"1": ("Enter the cave", "TREASURE"),
"2": ("Go back to forest", "START")
}
},

"RIVER": {
"text": "A strong river blocks your path.",
"choices": {
"1": ("Swim across", "CROCODILE"),
"2": ("Follow the river", "VILLAGE")
}
},

"TREASURE": {
"text": "Inside the cave you find hidden treasure. YOU WIN!",
"choices": {}
},

"CROCODILE": {
"text": "A crocodile attacks you. GAME OVER!",
"choices": {}
},

"VILLAGE": {
"text": "You discover a peaceful village. YOU SURVIVED!",
"choices": {}
}

}

# -----------------------------
# CREATE PLAYER
# -----------------------------

def create_player():

    name = input("Enter your name: ")

    player = Player(
        name=name,
        location="START"
    )

    session.add(player)
    session.commit()

    return player

