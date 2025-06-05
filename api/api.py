from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cricketpositionguesser.game import Game
from cricketpositionguesser.position_selector import PositionSelector
from cricketpositionguesser.positions import CricketPositions
import uuid

app = FastAPI()

origins = [
    "http://localhost:*",
    "http://127.0.0.1:*"
    "http://localhost:5173",
    "http://localhost:5173/game",
    "http://localhost:5173/guess"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for games
games = {}


class GameCreated(BaseModel):
    game_id: str


class GameGuess(BaseModel):
    game_id: str
    guess: str


class GameGuessResult(BaseModel):
    guess: str
    status: str
    distance_rating: str


@app.post("/game/", response_model=GameCreated)
def create_game():
    game_id = str(uuid.uuid4())
    cricket_positions = CricketPositions()
    cricket_positions_selector = PositionSelector(cricket_positions)
    game = Game(cricket_position_selector=cricket_positions_selector)

    games[game_id] = game

    return GameCreated(game_id=game_id)


@app.post("/game/guess", response_model=GameGuessResult)
def guess(request: GameGuess):

    game = games[request.game_id]
    result = game.make_guess(request.guess)

    return GameGuessResult(
        guess=result.guess,
        status=result.status,
        distance_rating=str(result.distance_rating) if result.distance_rating is not None else "N/A"
    )
