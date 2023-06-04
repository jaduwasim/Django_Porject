from django.contrib import admin
from testapp.models import first_parent, second_parent, child

# Register your models here.
admin.site.register(first_parent)
admin.site.register(second_parent)
admin.site.register(child)