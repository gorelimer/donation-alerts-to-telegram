from pathlib import Path
from typing import Any

import yaml


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwds)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self, **kwds) -> None:
        self.__dict__.update(kwds)

    @classmethod
    def from_path(cls, path: Path) -> "Config":
        data = yaml.load(path.read_text("utf-8"), yaml.FullLoader)
        if data is None:
            raise Exception("config is none")

        return cls(**data)


Config.from_path(Path("config.yml"))
