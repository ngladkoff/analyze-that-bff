from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from core import get_req

# Import Endpoints
from services.dummy.v1 import dummy_v1


# FAST API APP
app = FastAPI()


# CORS configuration
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

# Endpoints Routes
app.include_router(dummy_v1.router)


# Default page
@app.get("/")
def read_root(request: Request):
    url = request.url
    return {
        "Description": "Analyze-That-BFF",
        "Docs": f"{url}docs"
        }


@app.get("/secured")
# def get_secured(user: Auth0User = Security(get_auth0().get_user)):
def get_secured(q: str, req: dict = Depends(get_req)):
    return {
        "req": f"{req}",
        "q": q
    }
