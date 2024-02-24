## Synopsis

## Updated 2/2024

This application was a fork from the Appointment Scheduler by https://github.com/Rubamhassan.  As time
progressed it became a re-write of the original app mainly with the move to Python 3 and making a
generic booking service.  It has now been deemed to remove the fork of the original and let this application
live in its active repository.

The goal of the application is to be a generic plugin for other platforms and standalone to provide
the ability to book and track appointments managed by the user of the platform.  

Having this feature as part of any business can maximize any business that requires clients to book appointments.
A turn-key solution that will integrate with their system or have as a standalone system.  

The key component is the calendar which will update in real time and show appointments as well as available slots.
This calendar will be fully customizable to handle any business owner's needs in how they need booking services.

The idea is that a client can book and see their appointments for that business.  As well as the business
owner can see all their appointments.  In addition to this, a notification system is configurable to 
remind of such appointments.

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

Appointment App uses a Twilio API for text messaging to confirm the scheduled appointments.

## Tests

Tests for Appointment App are located in testing.py. Appointment App offers 56% test coverage through unit tests. Testing covers assertions on all pages of Appointment App, and ensures that when a user moves from one HTML to another it displays the correct page.

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, HTML, CSS, Coverage 


