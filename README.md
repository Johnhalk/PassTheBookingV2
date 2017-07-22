# PassTheBooking

## Introduction
This is a web application built in Python and the Model-View-Controller web framework Django.

## Core features:
Built in Django:
- Core models: Home, Client, Property, Booking and Django User administration.
- Stores and displays information from a database on to a webapp, dependant on individual models.
- SQLite database

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
## Technologies and Dependencies

**Core**
- Python
- Django
- Pip

**Testing**

- unittest


## Installation and Usage

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
myvenv/bin/activate
```
Update to the latest version of pip:
```
pip install --upgrade pip
```
Install Django with the following in the command line:
```
pip install django~=1.10.0
```
**Database**

Each model has its own fixture files to populate the database:

- booking/fixtures/initial_data.json
- property/fixtures/initial_data.json
- book_property/fixtures/initial_data.json

To load these files directly into your database type the following into the command-line:
```
python manage.py loaddata property/fixtures/initial_data
python manage.py loaddata booking/fixtures/initial_data
python manage.py loaddata book_property/fixtures/initial_data
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
