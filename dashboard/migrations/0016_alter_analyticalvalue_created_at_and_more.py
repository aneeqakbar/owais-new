# Generated by Django 4.0.3 on 2022-03-27 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_analyticalvalue_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyticalvalue',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 9, 25, 38, 369192)),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 9, 25, 38, 386106)),
        ),
    ]