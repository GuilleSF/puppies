# MarkDown file
# Api for dogs recognition with Flask and Keras
## version == 
#


This implement a Flask api which revive a POST request with an image as parameter and response with a json with a top 5 rated breeds.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You must have Python 3 (3.8.5) and the next libraries:

aniso8601==9.0.0
autoenv==1.0.0
click==7.1.2
Flask==1.1.2
Flask-RESTful==0.3.8
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
python-dotenv==0.15.0
pytz==2021.1
redis==3.5.3
rq==1.7.0
six==1.15.0
Werkzeug==1.0.1


```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

First we must install the libreris in the above section, "Prerequisites", how? Lets see:

Opening a terminal and tyoe:

```
git clone git@github.com:GuilleSF/puppies.git
```
Installing prerequisites:

```
utils/init.sh
export FLASK_APP=main.py
```
In other terminal

```
redis-server
```

In other terminal

```
python3.8 worker.py
```

End with an example of getting some data out of the system or using it for a little demo

In other terminal

```
curl -X POST -F \"image=@/path_to_image_dog/image.jpg\" localhost/api/breed
```

## Running the tests

Simple test, manually using the terminal

### Break down into end to end tests
Test for url status code response

```
python -m unittest
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system



## Authors

* **Guillermo Nieto Barba** 


