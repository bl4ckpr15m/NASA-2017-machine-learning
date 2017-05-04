# Great Gatsvim
The only thing you need to test our app is an Android device with Android lollipop or higher version installed. Download our [last signed apk](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0/releases/download/1.0/app-release.apk) and get fun.
## MENU
* [The idea](https://github.com/TheGreatGatsvim/NASA-April-2017#the-idea)
  * [How does it work?](https://github.com/TheGreatGatsvim/NASA-April-2017#how-does-it-work)
  * [How do we build it?](https://github.com/TheGreatGatsvim/NASA-April-2017#how-do-we-build-it)
  * [The future](https://github.com/TheGreatGatsvim/NASA-April-2017#the-future)
* [Prerequisites](https://github.com/TheGreatGatsvim/NASA-April-2017#prerequisites)
* [Install](https://github.com/TheGreatGatsvim/NASA-April-2017#install)
* [Run](https://github.com/TheGreatGatsvim/NASA-April-2017#run)
* [API](https://github.com/TheGreatGatsvim/NASA-April-2017#api)
* [Screenshots](https://github.com/TheGreatGatsvim/NASA-April-2017#screenshots)
* [Demo](https://github.com/TheGreatGatsvim/NASA-April-2017#demo)
* [Video](https://www.youtube.com/)

## The idea

### How does it work?
As soon as you open the app you will see your score. When you scan a new object, depending on what kind of material is it made of, you will get a different score. The manufacture of plastic emit more CO2 than the manufacture of paperboard, in this case you will get a higher score if you recycle plastic than if you recycle paperboard.

If you don't know if a particular object can be recyclable you can scan it with our app and you will see if it is or it isn't. Also, if it is recyclable, you will see he color of the container were the object must be recycle. 

### How do we build it?
We are aware that are more smartphones connected to the internet than computers, so we decided to create a native app for Android. However this is not the final project. We build​ an API so in the future we could build an IOS app, web app or even a robotic arm to help companies to recycle.

First we need the power of an artificial intelligence, we wanted this AI learn and become smarter. A great start point is [Tensorflow](https://www.tensorflow.org/), our server is build in python3 with [django](https://www.djangoproject.com/), great news cause Tensorflow run in python.

We manage to create asynchronous tasks ([redis](https://redis.io/)) to let our AI self learning. The more you use our artificial intelligence, smarter it becomes.

### The future


## Prerequisites
* Python 3
  * pip
  * virtualenvwrapper 
* Redis
* git
* docker

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
![api](https://s3-eu-west-1.amazonaws.com/family-page/jorge/nasa2017/Screenshot_20170502_171858.png)

|  Method  |              Description                  |
| -------- | ----------------------------------------- |
| `GET`    | Get a resource or get a list of resources |
| `POST`   | Create a control                          |

### Endpoint
##### [GET] /picture/
###### Request
```zsh
$ curl -H "Content-Type: application/json" -i http://nasa2017.jorgechato.com/picture/
```
```json
-H "Content-Type: application/json"
```
###### Response
```json
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Wed, 03 May 2017 09:02:40 GMT
Content-Type: application/json
Content-Length: 2635
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
Vary: Accept, Cookie, Accept-Encoding
Allow: GET, POST, OPTIONS

[{"pk":63,"feature":"http://nasa2017.jorgechato.com/media/raw/aLsaiaDFqC.jpg","label":"","score":0,"co2":null,"recyclable":false,"created_at":"2017-05-02T21:01:28.956238Z"},...]
```
##### [POST] /picture/
###### Request
```zsh
$ curl -H "Content-Type: application/json" -i http://nasa2017.jorgechato.com/picture/ -X POST --data '{feature:<picture>}'
```
```json
-H "Content-Type: application/json"
```
###### Response
```json
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Wed, 03 May 2017 09:02:40 GMT
Content-Type: application/json
Content-Length: 2635
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
Vary: Accept, Cookie, Accept-Encoding
Allow: GET, POST, OPTIONS

{"pk":63,"feature":"http://nasa2017.jorgechato.com/media/raw/aLsaiaDFqC.jpg","label":"","score":0,"co2":null,"recyclable":false,"created_at":"2017-05-02T21:01:28.956238Z"}
```
## Screenshots
<img src="https://s3-eu-west-1.amazonaws.com/family-page/jorge/nasa2017/photo_2017-05-03_11-15-34.jpg" height="400px"/>
<img src="https://s3-eu-west-1.amazonaws.com/family-page/jorge/nasa2017/photo_2017-05-03_11-15-30.jpg" height="400px"/>
<img src="https://s3-eu-west-1.amazonaws.com/family-page/jorge/nasa2017/photo_2017-05-02_17-19-52.jpg" height="400px"/>

## Demo
You can test the api by clicking on [nasa2017.jorgechato.com](http://nasa2017.jorgechato.com). However if you would like to test the all functionality of our project we recommend you to install [the last signed apk](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0/releases/download/1.0/app-release.apk) (only for Android).

You can also see the Android application project, it is build on java. Ready to use in all android devices with lollipop or higher version installed. [https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0](https://github.com/TheGreatGatsvim/NASA-April-2017-Android2.0)

