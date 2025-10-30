.PHONY: dev tests

all:


setup-local:
	python3 -m venv venv
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements/requirements.app.txt

# Dev commands
dev-server-local:  # dev-server-local port=8080
	python api.py $(port)

test:
	pytest tests

lint-check:
	-flake8 src/ tests/
	-isort -c src/ tests/
	-black --check src/ tests/

lint:
	isort src/ tests/
	black src/ tests/

