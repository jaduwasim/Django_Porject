from django.contrib import admin
from .models import Department, Employee
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name','dept_code']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_name','uidai','department','salary']