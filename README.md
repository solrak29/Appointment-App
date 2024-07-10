## Synopsis
  
Appointment Scheduler is an app that a business to service clients to schedule appointments.

The app will track all apopintments and availability as set by the business owner.  Users have
to create an account and be verfied by the business owner.  Once verified the client can request
appointments.  

This can maximize the office production as it gives the Clients the (freedom) opportunity to 
schedule their appointments when they are able to and at the time that is convenient for them. 

The calendar set-up with datetime shows real time dates and only allows the user to schedule 
two business days in advance. My calendar has the benefit of having two views: one for the Client 
and one for the doctor. The doctor has the added benefit of seeing who has scheduled an 
appointment at any time, both in the office and remotely.

<!--
/*
![homepage](/static/homepage.jpeg?raw=true "Homepage")

Client Log in:
![Client login](/static/Clientlogin.jpeg?raw=true "Client Log in page")

Once user is logged in:
![User page](/static/onceuserloggedin.jpeg?raw=true "Once user is logged in")

Schedule view for Client: 
![Schedule view for Client](/static/Clientscheduleview.jpeg?raw=true"Schedule view for Client")

Confirmed page:
![Confirmed page](/static/confirmedpage.jpeg?raw=true "Confirmed page")

Provider Log in page:
![Provider log in page](/static/providerloginpage.jpeg?raw=true "Provider Log in page")

Schedule view for the doctor:
![schedule view for the doctor](/static/doctorsview.jpeg?raw=true "Schedule view for the doctor")
*/

## Installation
Appointment App requires a requirements.txt file installation. Appointment App runs through the server.py file on http://localhost:5000/
-->

## Update 2024/07/06
Revisiting this project to start tracking and getting to MVP.
1. Creating a new user in the system and allowing new user to login.
2. Login should take to user page.

## Update 2023/4/4

This applications was built on python 2.7.  
I updated the source files to python 3. 

2to3-2.7 -w *.py to get thing udpated.

NOTE:  I ran this on python 3.11

the requiresments.txt needs to be updated, and I created a separate one with _ubuntu.txt.  These are installs required to run.
you will also need basic tools on ubuntu if you do not have them setup:

NOTE the first number there is not typed, it's the order in which I installed.

  234  sudo apt-get install libpq-dev
  232  sudo apt-get install python3.11-dev
  229  sudo apt-get install python-dev
  227  sudo apt-get install python3-dev
  223  sudo apt install build-essential
  165  sudo apt install postgresql
  115  sudo apt update


## API Reference

Appointment App is using a Twilio api for text messaging to confirm the scheduled appointments.

## Tests

Tests for Appointment App are located in testing.py . Appointment App offers 56% test coverage through unittests. Testing covers assertions on all pages on Appointment App, and ensures that when a user moves from one html to another it displays the correct page.

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, , HTML, CSS, Coverage 


