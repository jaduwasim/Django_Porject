# Generated by Django 4.1.5 on 2023-01-29 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='Name',
            new_name='First_Name',
        ),
    ]
