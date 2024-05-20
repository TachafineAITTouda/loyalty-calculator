up:
	cp -f .env.dev-sample .env.dev
	docker-compose up
down:
	docker-compose down
reset-django:
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py createsuperuser