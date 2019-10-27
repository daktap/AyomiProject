from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    def __str__(self):
        return super(User, self).__str__()
    
