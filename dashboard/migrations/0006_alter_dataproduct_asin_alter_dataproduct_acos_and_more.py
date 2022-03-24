# Generated by Django 4.0.3 on 2022-03-20 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_dataproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataproduct',
            name='ASIN',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Acos',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Ad_Group_Default_Bid',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Ad_Group_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Ad_Group_Name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Ad_Group_State',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Ad_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Bid',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Bidding_Strategy',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='CPC',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Campaign_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Campaign_Name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Campaign_State',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Click_through_Rate',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Clicks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Conversion_Rate',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Daily_Budget',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='End_Date',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Entity',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Impressions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Keyword_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Keyword_Text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Match_Type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Operation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Orders',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Percentage',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Placement',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Portfolio_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Product',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Product_Targeting_Expression',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Product_Targeting_Id',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='ROAS',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Resolved_Product_Targeting_Expression',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='SKU',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Sales',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Spend',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Start_Date',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='State',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Targeting_Type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='Units',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 19, 7, 5, 743861)),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='placementProductPage',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='placementTop',
            field=models.TextField(blank=True),
        ),
    ]
