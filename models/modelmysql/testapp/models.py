from django.db import models

# Create your models here.

from operator import mod
from statistics import mode
from tokenize import Number
from django.db import models

# Create your models here.
class Employees(models.Model):
    Employee_No=models.IntegerField()
    Eoployee_Name=models.CharField(max_length=64)
    Employee_Salary=models.FloatField()
    Employee_Address=models.CharField(max_length=64)

    class Meta:
        db_table = 'EMPLOYEE'


class Jobs(models.Model):
    Posting_Date=models.DateField()
    Location=models.CharField(max_length=54)
    Offered_Salary=models.FloatField()
    Qualification=models.CharField(max_length=54)
    class Meta:
        db_table = 'JOBS'


class Books(models.Model):
    Number=models.IntegerField()
    Title=models.CharField(max_length=64)
    Author=models.CharField(max_length=64)
    Publish_Date=models.DateField()
    class Meta:
        db_table = 'BOOKS'


class Customers(models.Model):
    Name=models.CharField(max_length=64)
    Account_Number=models.IntegerField()
    Mail_Id=models.CharField(max_length=64)
    Phone_Number=models.IntegerField()
    Age=models.IntegerField()
    class Meta:
        db_table = 'CUSTOMERS'
