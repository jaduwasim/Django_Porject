from django.db import models

# Create your models here.
# 1. Abstract Base class model inheritance:
class ContactInfo(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField()
    Address = models.CharField(max_length=64)

    class Meta:
        abstract = True
    
class Student(ContactInfo):
    Marks = models.IntegerField()
    Roll_NO = models.IntegerField()

class Teacher(ContactInfo):
    Subject = models.CharField(max_length=30)
    Salary = models.FloatField()

# Multi table Inheritance:
class ContactInfo2(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField()
    Address = models.CharField(max_length=64)
    
class Student2(ContactInfo2):
    Marks = models.IntegerField()
    Roll_NO = models.IntegerField()

class Teacher2(ContactInfo2):
    Subject = models.CharField(max_length=30)
    Salary = models.FloatField()
