# cas-testbed
A mock showcasing CAS authentication between a server and some client applications

This project's aim is to have a working mock up of a [CAS](https://en.wikipedia.org/wiki/Central_Authentication_Service) implementation using Django (although other CAS client implementations in order languages/frameworks are welcome). It can then be used as a base for anybody looking to implement all or parts of this in their environments.

There are currently three directories (three applications) present:

- casserver: The CAS server
- casclient1: CAS client
- casclient2: CAS client

The reason for there being two CAS clients, is so you can see that CAS is working. After logging into one client, try to log into the other one and no username/password will be required (the second CAS client will ask for a token from the CAS server, and you will be logged). The similar holds true for logging out: the CAS protocol implements Single-Sign-Out, so logging out of one client also logs you out of the other one.

## Requirements

At the moment, the project is aimed at Python-3.6 and Django-2.0. The additional packages required are [django-mama-cas](https://github.com/jbittel/django-mama-cas) for the server-side CAS, and [django-cas-ng](https://github.com/mingchen/django-cas-ng) for the client-side CAS. Both, as well as Django, can be installed via pip. The use of a [virtualenv](https://docs.python.org/3/library/venv.html) is **heavily recommended**:

~~~
# pip install django django-mama-cas django-cas-ng
~~~

**Note:** as of this writing (2018-01-22) *django-mama-cas* does not support Django 2.0. There is a [PR](https://github.com/jbittel/django-mama-cas/pull/56) adding support for it but it's not currently merged. For proper usage of this project, until the PR is fixed, it is recommended that you use [that branch](https://github.com/manelclos/django-mama-cas/tree/django-2.0-fixes). Alternatively, you can [patch it yourself](https://docs.djangoproject.com/en/2.0/releases/2.0/#python-compatibility) (it's not that hard ;).

## Installation

Once you have all the requirements and have cloned this repository, it can be installed/run by using these steps:

1. Set up and run the server:
~~~
cd casserver/
./manage.py migrate
./manage.py createsuperuser
~~~
2. Follow the onscreen instructions. Once the superuser has been created:
~~~
./manage.py runserver 127.0.0.1:8000
~~~
3. Log into http://127.0.0.1:8000/admin with the superuser account you have just created. Create as many users as you like.
4. Open another terminal and set up the first client (the previous runserver comamnd must be kept running):
~~~
cd casclient1/
./manage.py migrate
./manage.py runserver 127.0.1.1:8000
~~~
5. Do the same for the second client:
~~~
cd casclient2/
./manage.py migrate
./manage.py runserver 127.0.2.1:8000
~~~
6. Once everything is up and running, enter any of the clients' addresses and try to log in with one of the users you previously created. You should be redirected to a login webpage on the CAS server. After a successful login, you are redirected back to the original CAS client. At this point, you should be able to login on the second client automatically (you have to click 'log in' but you won't need to specify a username/password).

**Note:** while the server addresses are arbitrary, it is the way I have them configured by default. If you want to change it, bear in mind to also change accordingly:

- The **MAMA_CAS_SERVICES** variable in *casserver/casserver/settings.py*, pointing to the correct client CAS instances' IP addresses (or hostnames).
- In each CAS client, adjust the **CAS_SERVER_URL** variable in the relevant *settings.py* file.

## Notes

This is a personal project, with the only aim to be used as a guideline for future implementations. Things might change or break. User interface might be lacking.
