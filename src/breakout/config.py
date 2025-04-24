"""Global config options of the package."""

import os
from importlib import resources as pkg_resources
from pathlib import Path

from dotenv import load_dotenv

import breakout as project

load_dotenv()

PACKAGE_NAME = project.__name__

with pkg_resources.as_file(pkg_resources.files(project)) as package_dir:
    DEFAULT_CONFIG_FILE_PATH = package_dir / "logger_config.toml"

LOGGER_CONFIG_FILE = Path(os.environ.get("BREAKOUT_LOGGER_CONFIG_FILE", DEFAULT_CONFIG_FILE_PATH))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Breakout"
SCREEN_RESIZABLE = False
