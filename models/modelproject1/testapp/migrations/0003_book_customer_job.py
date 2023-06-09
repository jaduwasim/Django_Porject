# Generated by Django 3.2.9 on 2022-08-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20220830_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Title', models.CharField(max_length=64)),
                ('Author', models.CharField(max_length=64)),
                ('Publish_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Account_Number', models.IntegerField()),
                ('Mail_Id', models.CharField(max_length=64)),
                ('Phone_Number', models.IntegerField()),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Posting_Date', models.DateField()),
                ('Location', models.CharField(max_length=54)),
                ('Offered_Salary', models.FloatField()),
                ('Qualification', models.CharField(max_length=54)),
            ],
        ),
    ]
