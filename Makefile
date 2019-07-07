VENV_NAME=venv
BIN_PATH=$(VENV_NAME)/bin
PYTHON=$(BIN_PATH)/python
PYTHON_VERSION=python3.7
PIP=$(BIN_PATH)/pip
FLAKE8=$(BIN_PATH)/flake8
ISORT=$(BIN_PATH)/isort
SRC_PATH=src


all: run

virtualenv:
	test -d venv || virtualenv -p $(PYTHON_VERSION) venv
	$(PIP) install -r requirements.txt

run: virtualenv
	$(PYTHON) $(SRC_PATH)/app.py

clean:
	rm -rf venv/

isort-check:
	$(ISORT) --recursive --check-only $(SRC_PATH)

isort-fix:
	$(ISORT) --recursive $(SRC_PATH)

flake8-check:
	$(FLAKE8) $(SRC_PATH)

test: virtualenv isort-check flake8-check
