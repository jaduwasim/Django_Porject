from django.contrib import admin
from testapp.models import Person, Employe, Manager

# Register your models here.
admin.site.register(Person)
admin.site.register(Employe)
admin.site.register(Manager)