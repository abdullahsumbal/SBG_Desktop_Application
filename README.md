# SBG_Desktop_Application

We made a UI using PyQt and connected to the database using Python3 module named psycopg2.
The application is developed on a linux environment and deployed into a executable using Pyinstaller python3 module. The application can only run on linux system.
The Application code can be found on GitHub repository.

https://github.com/abdullahsumbal/SBG_Desktop_Application

The Application can perform the following options.
Option 1: Find the buildings in which bikes are used the most based on either (i) number of users for the bikes or (ii) the duration of bike sessions.
Option 2: Using the email of a bike user, we can find all the entire history of bookings they’ve ever made for a bike session.
Option 3: Adds a new bike to the database considering: what model the bike is, the last time the battery was charged, and whether it has a data collector or not.
Option 4: Shows all unresolved tickets for bikes for any selected bike manager.
Option 5: Modifies the password for a bike manager.
Using bike manager email and old password, we can insert a new password and modify it in the bikemanager table.
Option 6: Quit.

We will be demoing the application on Monday 26 March.

## Download the Application
git clone https://github.com/abdullahsumbal/SBG_Desktop_Application.git


## Run the Application
pyhton3 src/app.py

## Dependenices
Psycopg2
Pyhton3
Pyinstaller
PyQt
