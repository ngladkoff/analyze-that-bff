from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.dummy.v1 import dummy_v1

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dummy_v1.router)

@app.get("/")
def read_root():
    return {"Description": "Analyze-That-BFF"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
