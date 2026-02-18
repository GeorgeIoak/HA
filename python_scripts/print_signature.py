from homeassistant.components.recorder.statistics import async_import_statistics

code = async_import_statistics.__code__
args = code.co_varnames[: code.co_argcount]
logger.warning("async_import_statistics args: %s", args)