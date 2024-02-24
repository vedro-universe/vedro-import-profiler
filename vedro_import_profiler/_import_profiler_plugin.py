from typing import Type, Union

from vedro.core import ConfigType, Dispatcher, Plugin, PluginConfig
from vedro.events import ArgParsedEvent, ArgParseEvent, ConfigLoadedEvent

from ._scenario_file_loader import ScenarioFileLoader

__all__ = ("VedroImportProfiler", "VedroImportProfilerPlugin",)


class VedroImportProfilerPlugin(Plugin):
    def __init__(self, config: Type["VedroImportProfiler"]) -> None:
        super().__init__(config)
        self._global_config: Union[ConfigType, None] = None

    def subscribe(self, dispatcher: Dispatcher) -> None:
        dispatcher.listen(ConfigLoadedEvent, self.on_config_loaded) \
                  .listen(ArgParseEvent, self.on_arg_parse) \
                  .listen(ArgParsedEvent, self.on_arg_parsed)

    def on_config_loaded(self, event: ConfigLoadedEvent) -> None:
        self._global_config = event.config

    def on_arg_parse(self, event: ArgParseEvent) -> None:
        group = event.arg_parser.add_argument_group("Vedro Import Profiler")
        group.add_argument("--vedro-import-profiler", action="store_true",
                           help="Enable import profiler")

    def on_arg_parsed(self, event: ArgParsedEvent) -> None:
        if event.args.vedro_import_profiler:
            assert self._global_config is not None
            self._global_config.Registry.ScenarioLoader.register(ScenarioFileLoader, self)


class VedroImportProfiler(PluginConfig):
    plugin = VedroImportProfilerPlugin
