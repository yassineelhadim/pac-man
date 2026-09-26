.PHONY: install run debug clean lint lint-strict

SRC = pac-man.py pathfinder.py parser.py

install:
	@uv sync

run:
	@PYTHONPATH=. python3 src/pac_man.py config.json

debug:
	@python3 -m pudb pac-man.py config.json

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +

lint:
	@flake8 $(SRC)
	@mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs