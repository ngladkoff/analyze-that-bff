from db.repositories.base import BaseRepository
from models.game import GameCreate, GameUpdate, GameInDB


CREATE_GAME_QUERY = """
    INSERT INTO games (name, description)
    VALUES (:name, :description)
    RETURNING id, name, description;
"""


class GamesRepository(BaseRepository):
    """"
    All database actions associated with the Game resource
    """

    async def create_game(self, *, new_game: GameCreate) -> GameInDB:
        query_values = new_game.dict()
        game = await self.db.fetch_one(query=CREATE_GAME_QUERY, values=query_values)

        return GameInDB(**game)
