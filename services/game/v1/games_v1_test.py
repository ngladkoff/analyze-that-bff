import pytest
from typing import List, Union
from httpx import AsyncClient
from fastapi import FastAPI, APIRouter

from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_201_CREATED, HTTP_200_OK

from models.game import GameCreate, GameInDB

pytestmark = pytest.mark.asyncio

def test_games_true():
    assert 1 == 1

@pytest.fixture
def new_game():
    return GameCreate(
        name= "fake game name",
        description= "fake game description"
    )

class TestGamesRoutes:
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("v1_create_game"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    async def test_invalid_input_raises_error(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("v1_create_game"), json={})
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


class TestCreateGame:
    async def test_valid_input_creates_game(
        self, app: FastAPI, client: AsyncClient, new_game: GameCreate
    ) -> None:
        res = await client.post(
            app.url_path_for("v1_create_game"), json={"new_game": new_game.dict()}
        )
        assert res.status_code == HTTP_201_CREATED

        created_game = GameCreate(**res.json())
        assert created_game == new_game

    @pytest.mark.parametrize(
        "invalid_payload, status_code",
        (
            (None, 422),
            ({}, 422),
            ({"description": "test_description"}, 422),
        ),
    )
    async def test_invalid_input_raises_error(
        self, app: FastAPI, client: AsyncClient, invalid_payload: dict, status_code: int
    ) -> None:
        res = await client.post(
            app.url_path_for("v1_create_game"), json={"new_game": invalid_payload}
        )
        assert res.status_code == status_code


class TestGetGame:
    async def test_get_cleaning_by_id(self, app: FastAPI, client: AsyncClient, test_game: GameInDB) -> None:
        res = await client.get(app.url_path_for("v1_get_game_by_id", id=test_game.id))
        assert res.status_code == HTTP_200_OK
        game = GameInDB(**res.json())
        assert game == test_game


    @pytest.mark.parametrize(
        "id, status_code",
        (
            (500, 404),
            (-1, 404),
            (None, 422),
        ),
    )
    async def test_wrong_id_returns_error(
        self, app: FastAPI, client: AsyncClient, id: int, status_code: int
    ) -> None:
        res = await client.get(app.url_path_for("v1_get_game_by_id", id=id))
        assert res.status_code == status_code


    async def test_get_all_games_returns_valid_response(
            self, app: FastAPI, client: AsyncClient, test_game: GameInDB
        ) -> None:
            res = await client.get(app.url_path_for("v1_get_all_games"))
            assert res.status_code == HTTP_200_OK
            assert isinstance(res.json(), list)
            assert len(res.json()) > 0        
            games = [GameInDB(**l) for l in res.json()]
            assert test_game in games


class TestUpdateGame:


    @pytest.mark.parametrize(
        "attrs_to_change, values",
        (
            (["name"], ["new fake game name"]),
            (["description"], ["new fake game description"]),
            (["name", "description"], ["extra new fake game name", "extra new fake game description"]),
        ),
    )
    async def test_update_game_with_valid_input(
        self, 
        app: FastAPI, 
        client: AsyncClient, 
        test_game: GameInDB, 
        attrs_to_change: List[str], 
        values: List[str],
    ) -> None:
        game_update = {"game_update": {attrs_to_change[i]: values[i] for i in range(len(attrs_to_change))}}

        res = await client.put(
            app.url_path_for("v1_update_game", id=test_game.id),
            json=game_update
        )
        assert res.status_code == HTTP_200_OK
        updated_game = GameInDB(**res.json())
        assert updated_game.id == test_game.id  # make sure it's the same game
        # make sure that any attribute we updated has changed to the correct value
        for i in range(len(attrs_to_change)):
            assert getattr(updated_game, attrs_to_change[i]) != getattr(test_game, attrs_to_change[i])
            assert getattr(updated_game, attrs_to_change[i]) == values[i] 
        # make sure that no other attributes' values have changed
        for attr, value in updated_game.dict().items():
            if attr not in attrs_to_change:
                assert getattr(test_game, attr) == value


    @pytest.mark.parametrize(
        "id, payload, status_code",
        (
            (-1, {"name": "test"}, 422),
            (0, {"name": "test2"}, 422),
            (500, {"name": "test3"}, 404),
            (1, None, 422),
        ),
    )
    async def test_update_game_with_invalid_input_throws_error(
        self,
        app: FastAPI,
        client: AsyncClient,
        id: int,
        payload: dict,
        status_code: int,
    ) -> None:
        game_update = {"game_update": payload}

        res = await client.put(
            app.url_path_for("v1_update_game", id=id),
            json=game_update
        )
        assert res.status_code == status_code



# ...other code


class TestDeleteGame:


    async def test_can_delete_game_successfully(
        self, app: FastAPI, client: AsyncClient, test_game: GameInDB
    ) -> None:
        # delete the game
        res = await client.delete(app.url_path_for("v1_delete_game", id=test_game.id))
        assert res.status_code == HTTP_200_OK
        # ensure that the game no longer exists
        res = await client.get(app.url_path_for("v1_get_game_by_id", id=test_game.id))
        assert res.status_code == HTTP_404_NOT_FOUND


    @pytest.mark.parametrize(
        "id, status_code",
        (
            (500, 404),
            (0, 422),
            (-1, 422),
            (None, 422),
        ),
    )
    async def test_can_delete_game_with_invalid_input(
        self, app: FastAPI, client: AsyncClient, test_game: GameInDB, id: int, status_code: int
    ) -> None:
        res = await client.delete(app.url_path_for("v1_delete_game", id=id))
        assert res.status_code == status_code  

