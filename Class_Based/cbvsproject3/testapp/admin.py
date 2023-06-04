from django.contrib import admin
from testapp.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'ceo') # we can take both(list and tuple)
    # exclude = ('ceo',) #if your are takin only one field to exclude then comma is mandatory because its tuuple, we can take bothe(tuple and list)

admin.site.register(Company, CompanyAdmin)
