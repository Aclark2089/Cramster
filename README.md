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

You will need to make sure that your python has the correct modules installed
with pip. I recommend using pyenv to manage which python installation you are
running, but it is your choice. You will need to either setup a pyvenv, or
simply use your system wide python installation.

```
pyvenv 3.5.0 store_env <path-to-dir-where-you-want-to-install> #optional
pip install -r requirements.txt
```

Now that your python env is setup, you will either be able to clone the app/
folder or have to setup your own by running

```
django-admin startapp app #if you made your own venv
```

and then moving the models and configuration files in manually. I am still
trying to find a better way to clone a venv because the site-packages do not
allow for cloning into other locations.

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

Once you have the project repo cloned and make sure you have all of the
requirements.txt file installed all you should have to do is
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
pyvenv 3.5.0 store <path-dir>
pip install -r requirements.txt
django-admin startproject app #if you setup your own env, then you will just need to move the files around manually
```
