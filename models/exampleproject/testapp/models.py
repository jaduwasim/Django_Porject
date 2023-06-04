from django.db import models

# Create your models here.

class StudentModel(models.Model):
    First_Name = models.CharField(max_length=30)
    # Middle_Name = models.CharField(max_length=30)
    # Last_Name = models.CharField(max_length=30)