import os
from inspect import isclass
from pathlib import Path
from typing import Any, List, Type

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
            if self._is_vedro_scenario(val):
                val.__file__ = os.path.abspath(module.__file__)  # type: ignore
                loaded.append(val)
        return loaded

    def _path_to_module_name(self, path: Path) -> str:
        return path.with_suffix("").as_posix().replace("/", ".")

    def _is_vedro_scenario(self, val: Any) -> bool:
        if not isclass(val) or (val == Scenario):
            return False
        cls_name = val.__name__
        return issubclass(val, Scenario) and (
            cls_name.startswith("Scenario") or cls_name.endswith("Scenario"))
