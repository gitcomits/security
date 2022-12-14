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
The flaws are based on the [OWASP 2021 top 10 list](https://owasp.org/www-project-top-ten/) 

I would recommend to first read the list of flaws and the fixes to them for a better understanding of the application behaviour.
After that to try-out the application, apply the fixes (if available) and then to verify how the fixes changed the application behaviour.


## Flaws & Fixes

### Cross Site Request Forgery

Although Cross Site Request Forgery (CSFR) can not be found on the OWASP top 10 list it was still accepted as a flaw to this project.
CSFR is by default on in Django and many other frameworks and to create a situation where no CSFR token is required one must disable the CSFR line in the `settings.py`
  
[CSFR Flaw](https://github.com/gitcomits/security/blob/main/course/settings.py#L47) 
`https://github.com/gitcomits/security/blob/main/course/settings.py#L47`

Without a CSFR token it is possible to for a malicious third party to force a logged in user to perform unwanted actions. Depending on the user rights these unwanted acts might include the change of the users password, data theft or even deletion of crical files on server. 

To enable the CSFR token in Django remove the `#`, which comments the line, in the `settings.py`

[CSFR Fix](https://github.com/gitcomits/security/blob/main/course/settings.py#L47) 
`https://github.com/gitcomits/security/blob/main/course/settings.py#L47`

and also remove the `<!--` and `-->` from `home.html` to put in practice the CSFR token.

[CSFR Fix](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L20)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L20`












