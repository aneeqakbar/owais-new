# Generated by Django 4.0.3 on 2022-03-21 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_dataproduct_campaign_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyticalvalue',
            name='Campaign_Id',
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='Campaign_Id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analyticalvalue',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 20, 48, 12, 906886)),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 21, 20, 48, 12, 926872)),
        ),
    ]
