from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    ids=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    place=models.CharField(max_length=100)

class Employees(models.Model):
    name=models.CharField(max_length=100)
    ids=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)