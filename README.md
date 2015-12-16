# Cramster Bookstore

A Database Project for CIS4301 Project 1  
Authors: R. Alex Clark + Kevin Kimbrough  

## Assignment

__Requirements__
* Implement a website of a bookstore, creating the database modeled using this ![E/R Diagram](http://imgur.com/10D6Cet)
* This website and database need to implement ![these specifications](http://imgur.com/ymv0Dep)

These are the problems for the assignment that we tackled. The baseline problem was to implement a bookstore with set models (Users, Products, Suppliers, and Orders) with their given attributes.

## How We Chose To Solve The Problem

We have a bit a freedom with what tools we can use, the only limit being that we __cannot__ use a NoSQL database. The tools we considered were PHP, Ruby On Rails, and finally our eventual choice of Django with a MySQL backend implemented. We used a local MySQL database for most of the development process and created a production database on Amazon Web Services just for funzies.

### Project Specifications

* Problem 1 - Online Store
* Python using a custom virtualenv
* Django framework using Django Rest Framework
* MySQL DB setup using Amazon Web Services

### Due Date

This project was completed in the span of 1 month from November 9th, 2015 until the due date of December 3rd, 2015.    Thanksgiving and other holidays made collaboration difficult, in addition to the fact that Kevin's laptop was out of commision for the entire duration of the project meaning any changes he made required my testing afterwards to ensure that they did not break the build.  

__Final Grade:__ 100

### Postmortem

Really liked working on this project although I feel that the creation of an entire website is a bit out of the scope of this class. I had never used Django before and had barely touched Python, and working on this has gotten me interested in both topics.   

This project was hastily writted when we had time (I had a 16 credit workload Fall 2015 and Kevin is involved in many leadership positions around campus in addition to Computer Science Engineering) so I am sure going back over the code will make a more talented Django developer or experienced programmer cringe, but we had little time to worry about the polish and focused on mainly getting it to actually work.   

There was an optional requirement we did not have time to get done, and I would really liked to have finished writing up the html for all of the views, but it fufilled the criteria for a successful submission.   

All in all we killed this project and I am happy to have been able to learn Django from a class I did not expect to be doing much actual coding in besides making SQL statements.

If you would like to take a look at a simple Django project for school or any purpose, follow the setup instructions below.

***

### Setup Instructions

Clone the repository

```
git clone git@github.com:Aclark2089/Cramster.git
```

You will need to make sure that your python has the correct modules installed
with pip. I recommend using pyenv to manage which python installation you are
running, but it is your choice. You will need to either setup a pyvenv, or
simply use your system wide python installation.

```
pyvenv 3.5.0 Cramster_env
cd Cramster/
pip install -r requirements.txt
```

Running this will install all the necessary modules that the python environment needs. After all of this is done, you will finally be ready to use the app after connecting it to a MySQL Database (or whichever backend you decide to run with).


### Connecting to MySQL DB for Development

You will need to setup your own connection to your own MySQL Database. This can easily be accomplished in `app/app/settings.py` by editing the `DATABASES` given

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # This is where you would change the DB type
        'NAME': 'DATABASE_NAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOSTNAME',
        'PORT': 'PORT',
    }
}
```
Note that you can add multiple databases but that Django requires a `default` database in all cases.  
### Production Database Note
If you would like to see how to run a production database, I have already included a file `prod_database_example.py` in the app/ directory detailing how you can set that up. Simply dupe the file and drop the name to `prod_database.py` and setup your production database here under the name `default` still.  
__This database will always be used if this production database file has been created__

### Running the server

Once you have the project repo cloned and make sure you have all of the
requirements.txt file installed all you should have to do is
all you have todo to run the server is use:

```
cd app/
python manage.py runserver (can also be done using ./manage.py runserver)
```

This will run the server for you and you should be able to access it on the IP
given in the console window. You can additionally set the IP of where it will
run manually like so with `python manage.py runserver 0.0.0.10`

***

## Future Additions / Changes

If possible, I would really like to get this running on Docker, and actually put this onto a production server using Nginx. I attempted to do that at the beginning of the project but it proved too much to handle for the timeframe we worked with.

__Areas That Could Be Updated__
* Rewrite the views.py in store/ to be more readable and use class design instead of individual functions and checks for response type
* Django Rest Framework is implemented, but not to as full of an extent as it could be. Rewrite project with Django Rest Framework in mind for more than just the /api endpoint
* Figure out how Django uses session variables / context_processors to make a more consice and easy to manipulate 'cart' for adding multiple orders. This part of the project proved the most difficult simply because I did not find many docs on how this was implemented for Django


