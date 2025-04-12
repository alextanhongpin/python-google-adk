format:
	uvx ruff format

check:
	uvx ruff check --fix


web:
	open http://localhost:8000
	cd 001_quickstart && uv run adk web
