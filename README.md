# PassTheBooking
[Introduction](#introduction) | [Core](#core) | [Technologies](#technologies) | [Installation](#installation) | [Model Architecture](#models) | [Working Overview](#overview) |

## Introduction
This is a web application built in Python and the Model-View-Controller web framework Django.

## Core:
Built in Django:
- Core models: Home, Client, Property, Booking and Django User administration.
- Stores and displays information from a database on to a webapp, dependant on individual models.
- SQLite database
- Styling using CSS & Bootstrap

## User Stories
```

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to see a homepage displaying links to relevant work information.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to visit a wep app page that displays all my clients.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to click on a client and see more specific detail about my client.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to edit specific clients details if necessary and have that changed data store into the database.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to visit a wep app page that displays all properties.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to click on a property and see more specific detail about that property.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to edit specific details in a property if necessary and have that changed data store into the database.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to visit a wep app page that displays all bookings.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to click on a booking and see more specific detail about that booking.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to edit specific details in a booking if necessary and have that changed data store into the database.

As a PassTheBooking employee,
So that I can manage my workload,
I want to be able to visit the built in Django administritive user page.

As a PassTheBooking employee,
So that I can see who is employee of the month,
I want to be able to look at the homepage and see who it is.

```
## Technologies

**Core**
- Python
- Django
- Pip

**Testing**

- unittest

**Deployed on pythonanywhere**

```
http://johnashtonpython.pythonanywhere.com/
```


## Installation

Clone this repository and pull the files to a directory of your choosing via the command line.

**Installing Python**

- **Windows**
Go to Start menu → All Programs → Accessories → Command Prompt.
- **OS X**
Go to Applications → Utilities → Terminal.
- **Linux**
Go to Applications → Accessories → Terminal.

- This programme is written in Python, download Python for your computer below:
- [Windows](https://www.python.org/downloads/windows/)
- [Mac OS](https://www.python.org/downloads/release/python-351/)
- **Linux**
It is very likely Linux has Python already installed.

- To check you installed it correctly type the following into the command-line:
```
$ python --version
```
**Django Installation**

Activate the virtual environment with the following in the command-line:
```
source myvenv/bin/activate
```
Update to the latest version of pip:
```
pip install --upgrade pip
```
Install Django with the following in the command line:
```
pip install django~=1.10.0
```

**Create databases**

First run:
```
python manage.py migrate
```

This creates the databases for the project.

**Superuser creation**

We create a super user so we may access the Django built in administration User model. Type this into the command line then follow the prompts.  This will be used to log in to the administration page of the web app.
```
python manage.py createsuperuser
```

**Load data into database**

Each model has its own fixture files to populate the database:

- client/fixtures/initial_data.json - this holds the client model data
- property/fixtures/initial_data.json - this holds the property model data
- booking/fixtures/initial_data.json - this holds the booking model data

To load these files directly into your database type the following into the command-line:
```
python manage.py loaddata client/fixtures/initial_data
python manage.py loaddata property/fixtures/initial_data
python manage.py loaddata booking/fixtures/initial_data
python manage.py makemigrations
python manage.py migrate
```

Success! Your wep app is now up and running with a fully populated database.

Type the following into the command line:
```
python manage.py runserver
```

Now in a webbrowser of your choosing visit:
```
http://127.0.0.1:8000/
```

This will take you to the homepage of the web app.

## Testing

![Imgur](http://imgur.com/rXuWlS9.png)

Tests are ran using Djangos built in unittest framework.  There are 19 tests in total, tests are done on each apps views, models and forms. To run tests type the following into the command line:

```
python manage.py test
```


## Models:

![Imgur](http://imgur.com/cGguSOF.png)

**Client Model**
A client model Holds information about a client: Email, First name, Last name, Date joined, is staff and is active

**Property Model**
A property model holds information about a properties: Owner, Description of property, City Location, Address and number of bedrooms.  The property model holds a one-to-many relation with the Client model, stored within the Owner variable. A property must be connected to a client and a client can have many properties.

**Booking Model**
A Booking model holds information on bookings: Property of which the booking was made on, date of check in, date of check out, guest name.  The booking model holds a one-to-many relation with the Property model, stored within the property_booking variable.  A booking must be connected to a property and can have many bookings.

## Overview

## Homepage

The homepage displays all information in a navigation bar at the top to access Client, Property and Booking information, as well as django user administration. Be sure to scroll down!

![Imgur](http://imgur.com/Z2c0r8d.png)

## Client

Clicking on Client on the navbar takes the URL to 'http://127.0.0.1:8000/client/'.

![Imgur](http://imgur.com/95PWG2y.png)

This displays all relevant client information that is stored in the database - 13 client information populates the database via the fixture file.

Clicking on more information takes the url to 'http://127.0.0.1:8000/client/pk' where pk is a number that is associated to that client. For the database this ranges from 1 to 13 as there are 13 unique clients.  The page displays detailed information about the client as well as the properties that are registered to them. You can also access specific information about each property by clicking the 'More information on property:' link which takes you to that properties individual page: the url will be of the format http://127.0.0.1:8000/property/pk' and pk being that individual properties personal key.

![Imgur](http://imgur.com/N1Ovrzq.png)

Clicking on the edit symbol takes the user to an edit page: 'http://127.0.0.1:8000/client/pk/edit'.  In the screenshot below the url reads  'http://127.0.0.1:8000/client/1/edit' because the personal key for this client is 1.

![Imgur](http://imgur.com/wrhk0lI.png)


## Property

Clicking on Property on the navbar takes the URL to 'http://127.0.0.1:8000/property/'.

![Imgur](http://imgur.com/KIT8nfu.png)

This displays all relevant property information that is stored in the database - 20 properties populate the database via the fixtures file.

Clicking on more information takes the url to 'http://127.0.0.1:8000/property/pk' where pk is a number that is associated to that property. For the database this ranges from 1 to 20 as there are 20 unique properties.  The page displays detailed information about the property as well as the bookings made on that property. You can also access specific information about each booking by clicking the 'More information' link which takes you to that booking individual page: the url will be of the format 'http://127.0.0.1:8000/booking/pk' and pk being that individual properties personal key.

![Imgur](http://imgur.com/k7Hpmft.png)

Clicking on the edit symbol takes the user to the edit page 'http://127.0.0.1:8000/property/pk/edit'. In the screenshot below the url reads 'http://127.0.0.1:8000/property/4/edit' because the personal key for the property is 4.

![Imgur](http://imgur.com/rTCo0FW.png)

## Booking

Clicking on Booking on the nav bar takes the URL to 'http://127.0.0.1:8000/booking/'.

![Imgur](http://imgur.com/Zqp1rRl.png)

This displays all relevant information that is stored in the database - 32 bookings populate the database via the fixture file.

Clicking on more information takes the url to 'http://127.0.0.1:8000/booking/pk' where pk is a number that is associated to that booking. For the database this ranges from 1 to 32 as there are 32 unique bookings. The page displays detailed information about the booking.

![Imgur](http://imgur.com/NioSS3w.png)

Clicking on the edit symbol takes the user to the edit page 'http://127.0.0.1:8000/booking/pk/edit'. In the screenshot below the url reads 'http://127.0.0.1:8000/booking/7/edit' because the personal key for the property is 7.

![Imgur](http://imgur.com/iReekaw.png)

## Admin

Clicking on the Administration button on the nav bar takes the URL to 'http://127.0.0.1:8000/admin/'.  This displays all models and administrative groups for the web app.  You can only access this if you are a django superuser, as explained at the begining.

![Imgur](http://imgur.com/EU6H12a.png)


## The future?

- Building on the app in the future I would like to add a services model, storing all information about the cleaning facilities used for each property booking.  A service can have many properties and have many bookings and many clients.

-Re organise folder names, booking folder holding the client model and book_property folder holding the booking model doesn't make logical sense.
