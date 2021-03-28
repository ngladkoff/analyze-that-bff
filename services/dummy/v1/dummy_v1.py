from fastapi import APIRouter, Depends
from typing import Optional
from core import get_req

router = APIRouter(
    prefix="/api/v1/dummy",
    tags=["dummys"]
)

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
    return DUMMYS


@router.get("/{id}")
def read_dummy(id: int, q: Optional[str] = None):
    return {"id": id, "q": q}
