Create a virtual environment

python -m venv venv

Then active for windows

venv\Scripts\activate


Install process requirements package

pip install -r requirements.txt


Set up the database

python manage.py migrate


Create a superuser (admin login)

python manage.py createsuperuser


Run the development server

python manage.py runserver




