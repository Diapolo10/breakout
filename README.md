# project-name

Remember to:

1. Replace all instances of `project-name` with the real name of the project
2. Replace all instances of `breakout` with the "package name" of the project
3. Rename the source code folder from `breakout` to your package name
4. Generate a lock file (`uv sync`)
5. Rewrite the `README.md`
6. If the project is not an executable, delete the files:
   * `src/breakout/main.py`
   * `src/breakout/logger.py`
   * `src/breakout/logger_config.toml`
   * `src/breakout/config.py`
   * `python-dotenv` and `tomli` as dependencies in `pyproject.toml` (unless otherwise needed)
