from fastapi import APIRouter, Depends
from typing import Optional
from core.auth import get_req
from core import logger as core_logger


logger = core_logger.getLogger(__name__)
router = APIRouter()

DUMMYS = [
    {
        'id': 1,
        'name': 'dummy1'
    },
    {
        'id': 2,
        'name': 'dummy2'
    }
]


@router.get("/")
def read_dummys(commons: dict = Depends(get_req)):
    logger.info("v1_read_dummys")
    return DUMMYS


@router.get("/{id}")
def read_dummy(id: int, q: Optional[str] = None):
    return {"id": id, "q": q}
