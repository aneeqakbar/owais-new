# Generated by Django 4.0.3 on 2022-03-21 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_dataproduct_acos_remove_dataproduct_cpc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyticalvalue',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 6, 9, 55, 964784)),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 6, 9, 55, 981004)),
        ),
    ]
