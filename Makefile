VENV_NAME=venv
BIN_PATH=$(VENV_NAME)/bin
PYTHON=$(BIN_PATH)/python
PYTHON_VERSION=python3.7
ACTIVATE=$(BIN_PATH)/activate
PIP=$(BIN_PATH)/pip
FLAKE8=$(BIN_PATH)/flake8
ISORT=$(BIN_PATH)/isort
PYTEST=$(BIN_PATH)/pytest
SRC_PATH=src


all: run

virtualenv:
	test -d venv || virtualenv -p $(PYTHON_VERSION) venv
	$(PIP) install -r requirements.txt

run: virtualenv
	$(PYTHON) $(SRC_PATH)/app.py

run-heroku: virtualenv
	. $(ACTIVATE) && heroku local web

clean:
	rm -rf venv/

isort-check:
	$(ISORT) --recursive --check-only $(SRC_PATH)

isort-fix:
	$(ISORT) --recursive $(SRC_PATH)

flake8-check:
	$(FLAKE8) $(SRC_PATH)

pytest:
	$(PYTEST) $(SRC_PATH)

test: virtualenv isort-check flake8-check pytest
