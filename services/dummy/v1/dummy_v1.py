from fastapi import APIRouter

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
