
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
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
Visit List all the APIs documentation
[http://localhost:8080/docs/](http://localhost:8080/docs/)

Visit List all the APIs on localhost
[http://localhost:8080/api/](http://localhost:8080/api/)


