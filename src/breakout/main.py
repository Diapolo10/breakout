"""Main entry point, remove if project is not an executable."""

import logging

import arcade

from breakout.gui.main_menu import GameWindow, MainView
from breakout.logger import ROOT_LOGGER_NAME, setup_logging

logger = logging.getLogger(ROOT_LOGGER_NAME)


def main() -> None:
    """Run game."""
    setup_logging()
    window = GameWindow()
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
