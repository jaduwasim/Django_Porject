# Generated by Django 4.1.5 on 2023-02-14 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='first_parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=64)),
                ('f2', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='second_parent',
            fields=[
                ('f3', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('f4', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='child',
            fields=[
                ('second_parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='testapp.second_parent')),
                ('first_parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.first_parent')),
                ('f5', models.CharField(max_length=64)),
                ('f6', models.CharField(max_length=64)),
            ],
            bases=('testapp.first_parent', 'testapp.second_parent'),
        ),
    ]
