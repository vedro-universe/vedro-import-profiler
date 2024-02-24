from vedro_import_profiler import VedroImportProfiler, VedroImportProfilerPlugin


def test_plugin():
    plugin = VedroImportProfilerPlugin(VedroImportProfiler)
    assert isinstance(plugin, VedroImportProfilerPlugin)
