# Generated by Django 4.1.5 on 2023-07-31 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_emp_addr_employee_eaddr_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='employee_table',
        ),
    ]