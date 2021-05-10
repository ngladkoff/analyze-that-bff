from typing import Optional
from models.core import IDModelMixin, CoreModel


class GameBase(CoreModel):
    name: Optional[str]
    description: Optional[str]


class GameCreate(GameBase):
    name: str
    description: str


class GameUpdate(GameBase):
    ...


class GameInDB(IDModelMixin, GameBase):
    name: str
    description: str


class GamePublic(IDModelMixin, GameBase):
    ...
