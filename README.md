
TEAM GOLD SUBSCRIBER API
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

# install steps
```
1.make sure youve navigated to the folder containing the cloned files in your terminal
2.pip install -r requirements.txt
3.python manage.py migrate
4.python manage.py createsuperuser
5.python manage.py runserver

```
Visit List all the APIs documentation
[http://localhost:8080/docs/](http://localhost:8080/docs/)

Visit List all the APIs on localhost
[http://localhost:8080/api/](http://localhost:8080/api/)


