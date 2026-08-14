.PHONY: up down verify
up:
	docker compose up --build
down:
	docker compose down -v
verify:
	./scripts/verify.sh
