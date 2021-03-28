from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
