# Generated by Django 3.2.9 on 2022-08-30 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eaddr',
            new_name='Employee_Address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='eno',
            new_name='Employee_No',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='esal',
            new_name='Employee_Salary',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='ename',
            new_name='Eoployee_Name',
        ),
    ]
