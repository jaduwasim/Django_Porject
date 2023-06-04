from django.db import models

# Create your models here.
# 3. Multi Level Inheritance
class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

class Employe(Person):
    eno = models.IntegerField()
    esal = models.FloatField()

class Manager(Employe):
    exp = models.IntegerField()
    team_size = models.IntegerField()