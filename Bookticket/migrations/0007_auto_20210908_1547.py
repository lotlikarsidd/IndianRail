# Generated by Django 3.1.7 on 2021-09-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookticket', '0006_auto_20210907_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='Train_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
