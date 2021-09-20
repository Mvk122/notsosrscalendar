## An open source calendar of events for students

# Beginner programmer setup guide guide

## Installing dependencies: postgreSQL

One of required dependencies for most web projects is a database. In smaller projects, databases as files such as SQLite can be used however this can lead to issues and in the case of django, fewer features to work with in the long run. For this project we will be using postgreSQL that runs in the background (don't worry, it probably uses less system resources than just having a mouse plugged in)

* Step 1: Install postgreSQL  
* Step 2: Add psql (the command line for postgreSQL) to your PATH by adding the following to your PATH: `C:\Program Files\PostgreSQL\13\bin`
* Step 3: Check that the install worked by running `psql -U postgres` and logging in with the password you set during the install process 

## Installing dependencies: Python modules 

It is paramount that each python project has its own virtual environment with its own interpreter and dependencies. In the project directory type 

`python -m venv env`

To create a virtual environment in a new env folder (this folder is in the gitignore and will not be pushed to the repo). 

Activate your virtual environment with: 

`env\Scripts\activate`

Now that your environment is active, install the dependencies as stated in the `requirements.txt` using: 

`python -m pip install -r requirements.txt`

## Project specific setup: PostgreSQL database for the project

A database within postgreSQL needs to be created for your project and django requires a user to access that database hence, login to psql as previously done before and use the following commands: 

`create database [your_database_name];`

` create user [your_database_user] with encrypted password '[your_database_user_password]'`

`grant all privileges on database [your_database_name] to [your_database_user];`

Swap the variables in square brackets with your own names and passwords (do not include the brackets).

## Project specific setup: secrets.py 

The django project needs access to the user and the database that you created in the previous step, however the username and password for your database should not be commited to the public github repository, hence we need to create a secrets.py file that is included in the `.gitignore`

But first we need to generate a secret key for your django application. In the python interpreter use the following code to generate a random secret key: 

```python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

Create a file in the `notsosrscalendar` directory called secrets.py and place the following into the file: 

```python
secret_key = "the_secret_key_you_generated_earlier"
db_name = "the_db_name_from_earlier"
db_user = "the_db_username_from_earlier"
db_password = "the_db_password_from_earlier"
```

## Done!

The project setup is now done and you can run `python manage.py runserver` to run the django application locally!







