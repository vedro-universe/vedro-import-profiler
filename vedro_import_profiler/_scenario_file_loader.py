import os
from inspect import isclass
from pathlib import Path
from typing import List, Type

from vedro import Scenario
from vedro.core import ScenarioLoader

__all__ = ("ScenarioFileLoader",)


class ScenarioFileLoader(ScenarioLoader):
    async def load(self, path: Path) -> List[Type[Scenario]]:
        module_name = self._path_to_module_name(path)
        module = __import__(module_name, fromlist=[""])

        loaded = []
        for name in module.__dict__:
            if name.startswith("_"):
                continue
            val = getattr(module, name)
            if isclass(val) and issubclass(val, Scenario) and val != Scenario:
                val.__file__ = os.path.abspath(module.__file__)  # type: ignore
                loaded.append(val)
        return loaded

    def _path_to_module_name(self, path: Path) -> str:
        return path.with_suffix("").as_posix().replace("/", ".")
