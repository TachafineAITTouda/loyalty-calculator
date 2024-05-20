up: 
	if [ ! -f .env.dev ]; then cp .env.dev.example .env.dev; fi
	docker compose  --env-file .env.dev up  -d  --build
kill:
	docker compose down
