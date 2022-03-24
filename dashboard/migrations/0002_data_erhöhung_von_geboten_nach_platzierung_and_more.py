# Generated by Django 4.0.3 on 2022-03-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Erhöhung_von_Geboten_nach_Platzierung',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Gebotsstrategie',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Kampagnentargetingtyp',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Keyword_oder_Produkt_Targeting',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Produkt_Targeting_ID',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='Tagesbudget_der_Kampagne',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='sheet_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
