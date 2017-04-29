## Prerequisites
1. ruby 2.4
  * compass
  
2. Python 3
  * pip
  * virtualenvwrapper
  
3. Redis
4. git

## Install
I hardly recommend to install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
```bash
$ mkvirtualenv -p python3 nasa
$ pip install -r requirements.txt
```
## Run
```bash
$ python manage.py celery -A nasa worker -l debug -B
$ python manage.py runserver 0.0.0.0:8000
```
