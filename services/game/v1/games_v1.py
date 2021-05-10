from typing import Optional, List
from fastapi import APIRouter, Depends, Body, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from core.auth import get_req
from core import logger as core_logger

from models.game import GameCreate, GamePublic, GameUpdate
from db.repositories.games import GamesRepository
from services.dependencies.database import get_repository


logger = core_logger.getLogger(__name__)
router = APIRouter()


@router.get("/", name="v1_get_all_games", response_model=List[GamePublic])
async def get_all_games(
    games_repo: GamesRepository = Depends(get_repository(GamesRepository))
) -> List[GamePublic]:
    logger.info("v1_get_all_games")
    return await games_repo.get_all_games()


@router.get("/{id}", name="v1_get_game_by_id", response_model=GamePublic)
# async def get_game_by_id(id: int, commons: dict = Depends(get_req)):
async def get_game_by_id(id: int, games_repo: GamesRepository = Depends(get_repository(GamesRepository))) -> GamePublic:
    game = await games_repo.get_game_by_id(id=id)

    if not game:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No game found with that id")

    return game


@router.post("/", response_model=GamePublic, name="v1_create_game", status_code=HTTP_201_CREATED)
async def create_new_game(
    new_game: GameCreate = Body(..., embed=True),
    games_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GamePublic:
    created_game = await games_repo.create_game(new_game=new_game)
    return created_game


@router.put("/{id}/", response_model=GamePublic, name="v1_update_game")
async def update_game_by_id(
    id: int = Path(..., ge=1, title="The ID of the game to update."),
    game_update: GameUpdate = Body(..., embed=True),
    games_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GamePublic:
    updated_game = await games_repo.update_game(id=id, game_update=game_update)
    if not updated_game:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No game found with that id.")
    return updated_game


@router.delete("/{id}/", response_model=int, name="v1_delete_game")
async def delete_game_by_id(
    id: int = Path(..., ge=1, title="The ID of the game to delete."),
    games_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> int:
    deleted_id = await games_repo.delete_game_by_id(id=id)

    if not deleted_id:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No game found with that id.")

    return deleted_id
