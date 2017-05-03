# Great Gatsvim
The only thing you need to test our app is an Android device with Android lollipop or higher version installed. Download our [last signed apk](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0/releases/download/1.0/app-release.apk) and get fun.
## MENU
* [The idea]()
* [Prerequisites]()
* [Install]()
* [Run]()
* [API]()
* [Screenshots]()
* [Demo]()
* [Video](https://www.youtube.com/)

## The idea

## Prerequisites
1. Python 3
  * pip
  * virtualenvwrapper
  
2. Redis
3. git
4. docker

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
## API

### Endpoint

## Screenshots

## Demo
You can test the api by clicking on [nasa2017.jorgechato.com](http://nasa2017.jorgechato.com). However if you would like to test the all functionality of our proyect we recommend you to install [the last signed apk](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0/releases/download/1.0/app-release.apk) (only for Android).

You can also see the Android application project, it is build on java. Ready to use in all android devices with lollipop or higher version installed. [https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0)

