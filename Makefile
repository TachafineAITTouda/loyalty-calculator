up:
	cp -f .env.dev-sample .env.dev
	docker-compose up
down:
	docker-compose down
django-shell:
	docker-compose exec web bash
django-createsuperuser:
	docker-compose exec web python manage.py createsuperuser
django-migrate:
	docker-compose exec web python manage.py makemigrations loyalty
	docker-compose exec web python manage.py migrate
