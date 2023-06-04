# Generated by Django 4.1.5 on 2023-02-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=64)),
                ('Marks', models.IntegerField()),
                ('Roll_NO', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=64)),
                ('Subject', models.CharField(max_length=30)),
                ('Salary', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('contactinfo2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.contactinfo2')),
                ('Marks', models.IntegerField()),
                ('Roll_NO', models.IntegerField()),
            ],
            bases=('testapp.contactinfo2',),
        ),
        migrations.CreateModel(
            name='Teacher2',
            fields=[
                ('contactinfo2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.contactinfo2')),
                ('Subject', models.CharField(max_length=30)),
                ('Salary', models.FloatField()),
            ],
            bases=('testapp.contactinfo2',),
        ),
    ]
