# from os import environ
# import django
# environ.setdefault('DJANGO_SETTINGS_MODULE','FirstProject.settings')
# django.setup()
# from faker import Faker
# from testapp.models import Country, City
# f = Faker()
# from random import randint


from os import environ
import django
environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')
django.setup()

from testapp.models import Country

country = Country.objects.all()
print(country)