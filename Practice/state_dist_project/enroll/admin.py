from django.contrib import admin
from .models import Country, State, District
# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id','country_name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','state_name', 'country']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','district_name','state']