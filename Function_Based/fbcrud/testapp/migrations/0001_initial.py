# Generated by Django 4.1.5 on 2023-02-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('eaddr', models.CharField(max_length=64)),
                ('esal', models.FloatField()),
            ],
        ),
    ]
