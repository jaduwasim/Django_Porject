# first step, we shold follow this process in respective way
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ThirdProject.settings')
django.setup()

# Second Step, we shold done first step, the do this step:
from faker import Faker
from random import randint
from testapp.models import Employee

f = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1000,5000)
        fname = f.name()
        fesal = randint(10000,50000)
        feaddr = f.city()
        Employee.objects.get_or_create(eno=feno, ename=fname, esal=fesal, eaddr=feaddr)

n = int(input('Enter Number of Employee Records:'))
populate(n)
print(f'{n} Number of Employee has Inserted Successfully...')