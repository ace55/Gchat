The following technologies were used for the development of this project:
Windows/macOS(Recommended)
python3.8.2
pip
django 3.2.14 (LTS)
virtualenv
Redis
django channels 2
Postgres
Start with installing Python.
Welcome to Python.org

Install PIP
https://pypi.org/project/pip/
Open cmd prompt
pip install pip
Install HomeBrew for macOS:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

cd to project folder
Setup Virtual Environment:
python -m venv venv # second venv is the name of the virtualenv

cd venv
Activate the virtual environment:
Windows: Scripts\activate
Mac: source bin/activate

Install and setup PostgreSQL
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Setup a database and update the Setting.py file:

DB_NAME = "Your database Name"
DB_USER = "django"
DB_PASSWORD = "Your Password"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Start the PostgreSQL server.

python manage.py makemigrations # make database migrations
python manage.py migrate

Install Redis:
brew install redis
redis-server # to run redis server

Then pip install requirements.txt

Python manage.py runserver # to run the project
