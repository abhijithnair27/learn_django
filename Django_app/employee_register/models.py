from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    position = models.ForeignKey(position,on_delete=models.CASCADE)
