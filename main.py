from fastapi import FastAPI, Request
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
def read_root(request: Request):
    url = request.url
    return {
        "Description": "Analyze-That-BFF",
        "Docs": f"{url}docs"
        }
