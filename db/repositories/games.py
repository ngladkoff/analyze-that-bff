from typing import List
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from db.repositories.base import BaseRepository
from models.game import GameCreate, GameUpdate, GameInDB

CREATE_GAME_QUERY = """
    INSERT INTO games (name, description)
    VALUES (:name, :description)
    RETURNING id, name, description;
"""

GET_GAME_BY_ID_QUERY = """
    SELECT id, name, description
    FROM games
    WHERE id = :id;
"""

GET_ALL_GAMES_QUERY = """
    SELECT id, name, description
    FROM games;
"""

UPDATE_GAME_BY_ID_QUERY = """
    UPDATE games
    SET name         = :name,
        description  = :description
    WHERE id = :id
    RETURNING id, name, description;
"""

DELETE_GAME_BY_ID_QUERY = """
    DELETE FROM games
    WHERE id = :id
    RETURNING id;
"""


class GamesRepository(BaseRepository):
    """"
    All database actions associated with the Game resource
    """

    async def create_game(self, *, new_game: GameCreate) -> GameInDB:
        query_values = new_game.dict()
        game = await self.db.fetch_one(query=CREATE_GAME_QUERY, values=query_values)

        return GameInDB(**game)


    async def get_game_by_id(self, *, id: int) -> GameInDB:
        game = await self.db.fetch_one(query=GET_GAME_BY_ID_QUERY, values={"id": id})

        if not game:
            return None
        
        return GameInDB(**game)


    async def get_all_games(self) -> List[GameInDB]:
        game_records = await self.db.fetch_all(query=GET_ALL_GAMES_QUERY)
        return [GameInDB(**l) for l in game_records]


    async def update_game(self, *, id: int, game_update: GameUpdate) -> GameInDB:
        game = await self.get_game_by_id(id=id)
        if not game:
            return None
        game_update_params = game.copy(update=game_update.dict(exclude_unset=True))
        try:
            updated_game = await self.db.fetch_one(
                query=UPDATE_GAME_BY_ID_QUERY, values=game_update_params.dict()
            )
            return GameInDB(**updated_game)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid update params.")


    async def delete_game_by_id(self, *, id: int) -> int:
        game = await self.get_game_by_id(id=id)
        if not game:
            return None
        deleted_id = await self.db.execute(query=DELETE_GAME_BY_ID_QUERY, values={"id": id})
        return deleted_id
