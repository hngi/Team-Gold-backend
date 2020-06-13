SUBSCRIBER API
=========================
#### A dockerized micro-service for subscribing to a Saas app

Developer Setup
-------------------------------

Follow the following steps to setup your  dev environment

Get started with virtual env
----------------------------

Run the following commands to get started using virtualenv

``` shell
# once - create virtual environment
virtualenv env -p python3.6
```

# activate it
source env/bin/activate

# install deps
```
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver

```
Visit List all the APIs documentation
[http://localhost:8080/docs/](http://localhost:8080/docs/)

Visit List all the APIs on localhost
[http://localhost:8080/api/](http://localhost:8080/api/)



Alternatively, Get Started with PIP ENV 
----------------------------------------
Run the following commands to get started using virtualenv

``` shell
# once - Install Pip Library for the Virtual Enviroment
pip install pipenv
```

# activate it
``` shell
# once - create virtual environment
Pip shell
```
# install other dependencies
```
pipenv run install -r requirements.txt
pipenv run manage.py migrate
pipenv run manage.py makemigrations
pipenv run manage.py createsuperuser
pipenv run manage.py runserver 8080
```
