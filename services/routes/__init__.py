from fastapi import APIRouter

# Import routes
from services.dummy.v1.dummy_v1 import router as v1_dummy_router
from services.game.v1.games_v1 import router as v1_game_router

router = APIRouter()
router.include_router(v1_dummy_router, prefix="/v1/dummy", tags=["dummys"])
router.include_router(v1_game_router, prefix="/v1/games", tags=["games"])
