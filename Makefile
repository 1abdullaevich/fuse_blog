all: migrate run

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	manage.py runserver
