up:
	make setup
docker-up:
	docker-compose up
setup:
	pip install -e .
tests:
	pytest
lint:
	python3 -m flake8
fix-lint:
	black .
typer:
	python3 -m mypy

run:
	python3 -m agent_orchestra.startup

clean:
	rm -rf __pycache__ 
	rm -rf .pytest_cache 
	rm -rf .coverage

.PHONY: up down clean tests