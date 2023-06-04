from django.db import models

# Create your models here.


class first_parent(models.Model):
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)

class second_parent(models.Model):
    f3 = models.CharField(max_length=64, primary_key=True)
    f4 = models.CharField(max_length=64)

class child(first_parent, second_parent):
    f5 = models.CharField(max_length=64)
    f6 = models.CharField(max_length=64)
