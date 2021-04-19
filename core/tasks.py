from typing import Callable
from fastapi import FastAPI
from db import tasks as db_tasks
from . import logger as core_logger

logger = core_logger.getLogger(__name__)


def create_start_app_handler(app: FastAPI) -> Callable:
    logger.info("App Starting")

    async def start_app() -> None:
        await db_tasks.connect_to_db(app)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    logger.info("App Stoping")

    async def stop_app() -> None:
        await db_tasks.close_db_connection(app)
    return stop_app
