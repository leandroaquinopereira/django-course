# Django Course

### Install Packages
- pip install [name_package]

### Virtual Environment
- virtualenv: package that allow the virtual environments management

Commands:

``python -m virtualenv env``

``source env/bin.activate``

### Useful Commands 

- Install Packages:

`pip install -r requirements.txt`

- Django Project create:

`django-admin startproject proj .`

- Running :

`python manage.py runserver --settings=proj.settings_dev`

- Create a new app:

`django-admin startapp cadastros`

- Create the migrations to run on the DB :

`python manage.py makemigrations --settings=proj.settings_dev`

- Run changes on the DB:

`python manage.py migrate --settings=proj.settings_dev`

- Create a new superuser:

`python manage.py createsuperuser --settings=proj.settings_dev`


- Console with Django support:

```
import sys, os, django
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings_dev")
django.setup()
```

- Ipython install (other console): `pip install ipython`

- Use the proxy to build the image:

```
docker build -t sidia/local:1.0 --build-arg http_proxy=http://PROXY_IP:PROXY_PORT --build-arg https_proxy=http://PROXY_IP:PROXY_PORT .
docker image pull mdillon/postgis (+proxy)
docker image ls
```

For Reading
===

 - https://12factor.net/pt_br/
 - https://wiki.python.org.br/GuiaDeEstilo

