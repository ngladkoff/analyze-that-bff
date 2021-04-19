from databases import DatabaseURL
from starlette.config import Config
# from starlette.datastructures import Secret

config = Config(".env")

AUTH0_DOMAIN = config("AUTH0_DOMAIN", cast=str)
AUTH0_API_AUDIENCE = config("AUTH0_API_AUDIENCE", cast=str)
APP_TITLE = config("APP_TITLE", cast=str)
APP_VERSION = config("APP_VERSION", cast=str)
API_PREFIX = config("API_PREFIX", cast=str)
POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str)
POSTGRES_DB = config("POSTGRES_DB", cast=str)
DATABASE_URL = config(
  "DATABASE_URL",
  cast=DatabaseURL,
  default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa: E501
)
