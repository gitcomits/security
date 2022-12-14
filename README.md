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


### Cryptographic Failures (A02:2021)

[Flaw 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L41)

[Flaw 2](https://github.com/gitcomits/security/blob/main/secure/views.py#L11)

[Flaw 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57)

The *Cryptographic Failures* include non-encrypted data exposure. 
In the case of this app the inserted password data visible when inserting this, after that it is saved without encryption and then still it is shown in clear form on the page.   


[Fix 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L40)

The fixes for these flaws would be to change the `input type=text` to `input type=password' in the `home.html` file. This would prevent anybody from seeing the password when typing it in. 

Fix 2

Now the password is saved in plain text and it would need to be hashed. This could be achieved for example by using a hashing library like `passlib`. 
And then with the help of the library to hash the password before saving it
To install the library - `pip install passlib`
The hashing - `hashed_passwd = pbkdf2_sha256.encrypt(passwd, rounds=12000, salt_size=32)`

[Fix 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57)

It is against good practises to show passwords, to prevent this the line doing this should be commented or removed from `home.html` file.


### Injection (A03:2021)

[Flaw](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51)

This flaw includes exposure to un-sanitized data provided by a end-user. This can lead to very unwanted situations if the browser validates the data in non-wanted manner. This could lead to temporary or permanent data loss, or in a milder situation to a bad user experience. By defaiöt escaping special characters is turned on in Django but they can be turned of as well. 
For visual purposes you can enter `Hello &lt;i>my&lt;/i> World!` in the `First Name` and `Last Name` fields to see the differences.


To fix this, one needs to remove the `{% autoescape off %}` and `{% endautoescape %}` parts from the `home.html` file.

[Fix 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51)

[Fix 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L52)


### Insecure Design (A04:2021)


