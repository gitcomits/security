# Project Report for Cyber Security Base Course

## Background

This simple web application was produces as part of the Mooc Cyber Security Course. 
The goal of the application is to demonstrate some of the more popular OWASP flaws and their possible fixes.
Django web framework was used as base for this one (1) page application. The underlying database is sqlite3 which comes included in the 
Django framework. 


## Installation

If you have ***Djanogo web framwork*** and ***Python*** installed on a Linux based operating system no other installations will be required. 
With other operating system the process might differ. 
Depending of their antiquity you might have to update them to their current release version. 
After cloning this git find the folder which contains `manage.py` and execute the following: `python manage.py runserver`.
The application will start a local server which can be aaccesed by entering `http://localhost:8000/`. There is also an administrative area which can be located in `http://localhost:8000/admin`. 


## Instructions

As stated earlier the application is a one (1) page web application. It contains a form with five (5) different insert fields. 
When submitting the form the inserted data will be saved to an underlying sqlite3 database and displayed on the same page.
Because the task was to create a flawy web application the application might not work as expected. 
Below you will find the OWASP flaws and information on how to fix them.

I would recommend to first read the list of flaws and the fixes to them for a better understanding of the application behaviour.
After that to try-out the application, apply the fixes (if available) and then to verify how the fixes changed the application behaviour.
