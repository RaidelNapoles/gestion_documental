# Description

Django project to manage a journalistic repository

## Installation

```bash
# Create a virtual environment
python3 -m venv django_env

# Activate your virtual environment
source django_env/bin/activate

#install the project's dependencies
pip install -r requirements.txt

# Create a database in PostgreSQL for the application to use (for example, gestion_documental_db).

# Create a .env file inside gestion_documental/ folder and populate it with the PostgreSQL database settings (as shown in .envexample)

# Run database migrations
python3 manage.py migrate
```

## Running tha app

```bash
# Start the server
python3 manage.py runserver
```
