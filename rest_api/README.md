# Info
How to create a REST API using `python` and `flask`

## Requirements
- `flask-restful`


## Folders
- insomnia <br>
  Just some picture of the program `insomnia` (see below) which are displayed in the jupyter-notebook.



# Additional Information
## What is a REST API ?
 
 **REST** is an acronym for **RE**presentational **S**tate **T**ransfer, **API** **A**pplication **P**rogramming **I**nterface.
 
This means its an interface with a certain architecture that allows the communication between a **client** and a **server**, e.g. *you* with a *database* or a *user* with *your database*.

The REST architectural style were originally communicated by Roy Fielding in his doctoral dissertation (see https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).

If you want to learn more about:
* [What Is REST?](https://www.restapitutorial.com/lessons/whatisrest.html#)
* [Was ist eine REST API](https://www.cloudcomputing-insider.de/was-ist-eine-rest-api-a-611116/) (german)

As you may imagine this is an important way to automatically get data from servers or distribute data.

It normally can handle **requests** of the type
* **GET** - request data from the server
* **POST** - sends data to the server
* **PUT / PATCH** - changes data on the server
* **DELETE** - deletes existing data on the server

## Examples 
### Checkout: create a REST API
https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3

gist : https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a

##### install flask-restful
```
pip install flask-restful
```

##### download the gist**
```
wget https://gist.githubusercontent.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a/raw/360bf7651077145438214455842de8d2390906cb/app.py
```


## test a REST API with insomia
### Install insomnia
see https://support.insomnia.rest/article/23-installation


#### start it
```
insomnia
```

#### GET
Just a test request

1.) create a get request

2.) address = ```http://127.0.0.1:5000/user/Nicholas```
