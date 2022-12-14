from django.db import models

# Create your models here.

class Info(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.CharField(max_length=5)


# changes "object" to firs + lastname in django admin panel for db and return value

    def __str__(self):
        return self.fname + ' ' + self.lname 