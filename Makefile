.PHONY: run format quality-check test

run:
	@poetry run python src/main.py

format:
	@poetry run black .

quality-check:
	@poetry run flake8 .
	@poetry run black --check .

test:
	@echo "Hay que implementar los tests"
