from django.db import models

# Create your models here.

class Department(models.Model):
    dept_code = models.CharField(max_length=10)
    dept_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'department_table'
    
    def __str__(self) -> str:
        return f'{self.dept_name}'

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    uidai = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()

    class Meta:
        db_table = 'employee_table'

    def __str__(self) -> str:
        return f'{self.emp_name}'