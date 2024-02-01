deploy:
	python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
deploy-docker:
	clear
	docker-compose down -v
	sudo rm -rf docker/mysql/data
	docker-compose up --build -d
ssh-api:
	docker exec -it django_app_api /bin/bash
run-tests:
	python manage.py test -v 2 user_api.tests



