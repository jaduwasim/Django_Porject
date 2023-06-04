from django.contrib import admin
from testapp.models import Employees, Jobs, Books, Customers

# Register your models here.

# Employee Registaraion on Admin Panel &  List Display their Fields
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Employee_No','Eoployee_Name','Employee_Salary','Employee_Address']
admin.site.register(Employees, EmployeeAdmin)

# Jobs Registaraion on Admin Panel &  List Display their Fields
class JobsAdmin(admin.ModelAdmin):
    list_display=['Posting_Date','Location','Offered_Salary','Qualification']
admin.site.register(Jobs, JobsAdmin)

# Books Registaraion on Admin Panel &  List Display their Fields
class BooksAdmin(admin.ModelAdmin):
    list_display=['Number','Title','Author','Publish_Date']
admin.site.register(Books, BooksAdmin)

# Customer Registaraion on Admin Panel &  List Display their Fields
class CustomerAdmin(admin.ModelAdmin):
    list_display=['Name','Account_Number','Mail_Id','Phone_Number','Age']
admin.site.register(Customers, CustomerAdmin)