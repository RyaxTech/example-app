import importlib.metadata

try:
    __version__ = importlib.metadata.version(__package__)
except (NameError, importlib.metadata.PackageNotFoundError):
    __version__ = "dev"
