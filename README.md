# CIS4301 Project 1

R. Alex Clark + Kevin Kimbrough

### Project Specifications

* Problem 1 - Online Store
* Python using a custom virtualenv and Django framework
* MySQL DB setup using Amazon Web Services

***

### Installation Instructions

Clone the repository

```
git clone git@github.com:Aclark2089/db_store_project.git
```

Make sure that you set the python environment to the repository if you are at
the ***REMOVED*** of the project you can do it with:

```
source bin/activate
```

Django should already be installed in the project

***

### Connecting to MySQL DB

Make sure that you are able to connect to the MySQL database on AWS. Download
mysql and optionally get a GUI like SQL Developer or MySQL Workbench, and then
use the connection information

> Host: ***REMOVED***
>
> Port: 3306
>
> User: ***REMOVED***
>
> Password: ***REMOVED***

***

### Running the server

Once you have the project repo cloned and have sorced the python activate file,
all you have todo to run the server is use:

```
cd app/
python manage.py runserver
```

This will run the server for you and you should be able to access it on the IP
given in the console window. You can additionally set the IP of where it will
run manually like so with `python manage.py runserver 0.0.0.10`
***
##TLDR;
```
git clone git@github.com:Aclark2089/db_store_project.git
cd db_store_project
source bin/activate
```
