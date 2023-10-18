# Generated by Django 4.1.8 on 2023-10-17 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('population', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.country')),
            ],
            options={
                'db_table': 'city',
            },
        ),
    ]
