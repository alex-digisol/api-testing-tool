start:
	docker compose --env-file .env up -d --build

dev_start:
	docker compose --env-file .env -f docker-compose.dev.yml up -d --build