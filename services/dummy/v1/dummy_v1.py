from fastapi import APIRouter
from typing import Optional

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
def read_dummys():
    return DUMMYS

@router.get("/{id}")
def read_dummy(id: int, q: Optional[str] = None):
    return {"id": id, "q": q}

