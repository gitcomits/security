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
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L41`

[Flaw 2](https://github.com/gitcomits/security/blob/main/secure/views.py#L11)
`https://github.com/gitcomits/security/blob/main/secure/views.py#L11`

[Flaw 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57`

The *Cryptographic Failures* include non-encrypted data exposure. 
In the case of this app the inserted password data is visible when inserting it (Flaw 1), after that it is saved without encryption (Flaw 2) and then still it is shown in clear form on the page (Flaw 3).   


The fixes for these flaws would be to change the `input type=text` to `input type=password' in the `home.html` file. This would prevent anybody from seeing the password when typing it in. 

[Fix 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L40)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L40`


Now the password is saved in plain text and it would need to be hashed. This could be achieved for example by using a hashing library like `passlib`. 
And then with the help of the library to hash the password before saving it

Fix 2
To install the library - `pip install passlib`
The hashing - `hashed_passwd = pbkdf2_sha256.encrypt(passwd, rounds=12000, salt_size=32)`


It is against good practises to show passwords, to prevent this the line doing this should be commented or removed from `home.html` file.

[Fix 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L57`


### Injection (A03:2021)

[Flaw](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51`

This flaw includes exposure to un-sanitized data provided by a end-user. This can lead to very unwanted situations if the browser validates the data in non-wanted manner. This could lead to temporary or permanent data loss, or in a milder situation to a bad user experience. By defaiöt escaping special characters is turned on in Django but they can be turned of as well. 
For visual purposes you can enter `Hello &lt;i>my&lt;/i> World!` in the `First Name` and `Last Name` fields to see the differences.


To fix this, one needs to remove the `{% autoescape off %}` and `{% endautoescape %}` parts from the `home.html` file.

[Fix 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L51`

[Fix 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L52)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L52`

### Insecure Design (A04:2021)

[Flaw 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L31)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L31`

[Flaw 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L36)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L36`

[Flaw 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L41)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L41`

[Flaw 4](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L48)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L48`


Part of insecure design is flaws found in the application design. These can lead to unwanted data exposure, misuse off the application and extremely bad user experiences. In the application in question there are several design flaws: 

- no feedback if the form was saved or not
- no hashing of password on the form 
- no validation of the data in the fields (Flaw 1 - 3)
- in the case of no save the valid data is erased from the form
- showing too much data (Flaw 4)

Feedback can be given by adding information if the submitting was succesfull. To do this remove the `<!--` and `-->` from home.html

[Fix feedback 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L6)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L6`

[Fix feedback 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L15)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L15`


The password hashing can be fixed by changing the field type to `password` 

[Fix hashing](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L40))
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L40`

Validating the two other fields is done in similar manner, giving the age field type `number` and the email field type `email`.

[Fix 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L30)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L30`

[Fix 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L35)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L35`

For the data to remain in the form fields even the save would not be successfull they need to be replaced when page reloads. 
For this to be done both the `views.py` and the `home.html` needs to be edited. 

From the `views.py` uncomment both lines 20 and 21

[Fix fields 1](https://github.com/gitcomits/security/blob/main/secure/views.py#L20)
`https://github.com/gitcomits/security/blob/main/secure/views.py#L20`

[Fix fields 2](https://github.com/gitcomits/security/blob/main/secure/views.py#L21)
`https://github.com/gitcomits/security/blob/main/secure/views.py#L21`

and comment line 23.

[Fix fields 3](https://github.com/gitcomits/security/blob/main/secure/views.py#L23)
`https://github.com/gitcomits/security/blob/main/secure/views.py#L23`

Then in `home.html` uncomment the four value lines. 

[Fix values 1](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L23)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L23`

[Fix values 2](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L27)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L27`

[Fix values 3](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L32)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L32`

[Fix values 4](https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L37)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L37`

Do not forget to remove, the now redundant `>` sign from the previous line ends (i.e. lines 22, 26, 31, 36)

Not to show the previously data the `home.html` needs to further be edited.
Remove or comment starting from line 48 to and including line 59

[Fix 4](https://github.com/gitcomits/security/blob/main/s#L48ecure/templates/home.html#L48)
`https://github.com/gitcomits/security/blob/main/secure/templates/home.html#L48`

### Security Logging and Monitoring Failures (A09:2021)

Logging is an important part security. It helps to find both errors and intruders in the system, but only if the logs are monitored.

By default loggin is not turned on in Django. To do this one needs to create a configuration for loggin  in `settings.py` file.
There are several levels of logging in Django and for this example i have chosen the `DEBUG` level. 

The configuration is already in place (`settings.py` from line 129 forward), the only thing to activate it is to comment line 127 in the `settings.py` to activate it.

[Fix loggin](https://github.com/gitcomits/security/blob/main/course/settings.py#L127)
`https://github.com/gitcomits/security/blob/main/course/settings.py#L127`



