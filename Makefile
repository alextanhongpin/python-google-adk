include .env
export


marimo:
	uv run marimo edit


format:
	uv format


check:
	uvx ruff check --fix --select I
	uv run mypy


web:
	open http://localhost:8000
	cd 01_quickstart && uv run adk web


api:
	open http://localhost:8000
	cd 01_quickstart && uv run adk api_server


test:
	curl -X POST http://0.0.0.0:8000/apps/roulette_wheel/users/u_123/sessions/s_123 \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}' | jq


test_run:
	curl -X POST http://0.0.0.0:8000/run \
	-H "Content-Type: application/json" \
	-d @data/run.json | jq


test_run_sse:
	curl -X POST http://0.0.0.0:8000/run_sse \
	-H "Content-Type: application/json" \
	-d @data/run_sse.json
