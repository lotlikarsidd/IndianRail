# Generated by Django 3.1.7 on 2021-09-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookticket', '0009_auto_20210908_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='Arrival_Time',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='time',
            name='Departure_Time',
            field=models.TimeField(max_length=5),
        ),
    ]
