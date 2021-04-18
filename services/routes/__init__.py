from fastapi import APIRouter

# Import routes
from services.dummy.v1.dummy_v1 import router as v1_dummy_router

router = APIRouter()
router.include_router(v1_dummy_router, prefix="/v1/dummy", tags=["dummys"])
