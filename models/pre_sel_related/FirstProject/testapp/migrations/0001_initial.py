# Generated by Django 4.1.5 on 2023-10-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('hometown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth', to='testapp.city')),
                ('living', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citizen', to='testapp.city')),
                ('visitation', models.ManyToManyField(related_name='visitor', to='testapp.city')),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.province'),
        ),
    ]
