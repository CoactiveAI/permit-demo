# list all targets and exit
default: 
    just --list

# install python dependencies (in venv, via poetry)
install: 
    poetry install

# install python dependencies (in venv, via poetry) with dev extras
install-dev:
    poetry install --with dev

# update python dependencies (in venv, via poetry)
update:
    poetry update

# format python code
format:
    poetry run isort .
    poetry run black .
    poetry run ruff check --fix .

# lint python code
lint:
    poetry run flake8 .

# type python code
types:
    poetry run mypy .

# cleanup
cleanup: format lint types

# format, lint, and type check python code
validate: 
    poetry run isort --check-only .
    poetry run ruff check .
    poetry run mypy .

# test python code - unit
test *flags="":
    poetry run python -m pytest -vvv {{flags}}
