import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject1.settings')
import django
django.setup()

from testapp.models import Employee
data = Employee.objects.all()
print(str(data.query))