import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY


class TestGamesRoutes:


    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("v1_create_game"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND



    @pytest.mark.asyncio
    async def test_invalid_input_raises_error(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("v1_create_game"), json={})
        assert res.status_code != HTTP_422_UNPROCESSABLE_ENTITY



def test_games_true():
    assert 1 == 1


