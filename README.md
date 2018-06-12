# Secure Object Storage

## Installation

To run this application you must install python3, pip3, and mysql on your machine.

`sudo apt install python3 python3-pip mysql-server`

Then navigate to the app folder in the repository and run

`pip3 install -r ./app/requirements.txt`

This will install the Flask and MySQL libraries for python.

## Getting Started

### Flask

To start the application, navigate to the app folder in the repository and run 

`python3 app.py`

This should start a webserver on port 8080 on your local machine.

### MySQL

After installing MySQL, run it using 

`mysql -u [user] -p`

Then create a database called FlaskDB

`CREATE DATABASE FlaskDB;`

Once this is done you can quit mysql and create the neccessary tables and store procedures by navigating to the app directory and running

`mysql -u [user] -p < procedures.sql`

If you want to clear all procedures and tables run

`mysql -u [user] -p < clean.sql -f`

This may throw some errors or warnings if a table or procedure is already missing but it should continue to run and remove them all.

## Software Versions
On my (Alex Dawson) machine I am running:

-mysql  Ver 14.14 Distrib 5.7.21, for Linux (x86_64) using  EditLine wrapper

-Ubuntu 16.04.4 LTS 64-bit

-Python 3.5.2

-pip 9.0.1

## changed by Injung Kim
6/12/2018
