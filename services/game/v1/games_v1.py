from typing import Optional, List
from fastapi import APIRouter, Depends, Body
from starlette.status import HTTP_201_CREATED

from core.auth import get_req
from core import logger as core_logger

from models.game import GameCreate, GamePublic
from db.repositories.games import GamesRepository
from services.dependencies.database import get_repository


logger = core_logger.getLogger(__name__)
router = APIRouter()

GAMES = [
    {
        'id': 1,
        'name': 'juego1',
        'description': 'desc juego1'
    },
    {
        'id': 2,
        'name': 'juego2',
        'description': 'desc juego2'
    }
]


@router.get("/")
async def get_all_games() -> List[dict]:
    logger.info("v1_get_all_games")
    return GAMES


@router.get("/{id}", name="v1_read_game")
def read_game(id: int, q: Optional[str] = None, commons: dict = Depends(get_req)):
    return {"id": id, "q": q}


@router.post("/", response_model=GamePublic, name="v1_create_game", status_code=HTTP_201_CREATED)
async def create_new_game(
    new_game: GameCreate = Body(..., embed=True),
    games_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GamePublic:
    created_game = await games_repo.create_game(new_game=new_game)
    return created_game
