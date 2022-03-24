# Generated by Django 4.0.3 on 2022-03-12 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_data_erhöhung_von_geboten_nach_platzierung_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('P', 'Product'), ('B', 'Brand')], max_length=255)),
                ('Record_ID', models.TextField()),
                ('Datensatztyp', models.TextField()),
                ('Kampagnen_ID', models.TextField()),
                ('Kampagne_Kampagnename', models.TextField()),
                ('Kampagnentyp', models.TextField()),
                ('Anzeigenformat', models.TextField()),
                ('Budget', models.TextField()),
                ('Portfolio_ID', models.TextField()),
                ('Kampagnenstartdatum', models.TextField()),
                ('Kampagnenenddatum', models.TextField()),
                ('Budget_Typ', models.TextField()),
                ('URL_der_Landing_Page', models.TextField()),
                ('Landing_Page_ASINs', models.TextField()),
                ('Markenname', models.TextField()),
                ('Markenidentitäts_ID', models.TextField()),
                ('Markenlogo_Asset_ID', models.TextField()),
                ('Headline', models.TextField()),
                ('Anzeigendesign_ASINs', models.TextField()),
                ('Medien_ID', models.TextField()),
                ('Automatisierte_Gebote', models.TextField()),
                ('Gebotsfaktor', models.TextField()),
                ('Anzeigengruppe', models.TextField()),
                ('Max_Gebot', models.TextField()),
                ('Keyword', models.TextField()),
                ('Ubereinstimmungstyp', models.TextField()),
                ('Kampagnenstatus', models.TextField()),
                ('Bereitstellungsstatus', models.TextField()),
                ('Status_der_Anzeigengruppe', models.TextField()),
                ('Status', models.TextField()),
                ('Impressions', models.TextField()),
                ('Klicks', models.TextField()),
                ('Ausgaben', models.TextField()),
                ('Bestellungen', models.TextField()),
                ('Einheiten_insgesamt', models.TextField()),
                ('Verkäufe', models.TextField()),
                ('ACOS', models.TextField()),
                ('Platzierungstyp', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_brands', to='dashboard.client')),
            ],
        ),
        migrations.CreateModel(
            name='DataProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('P', 'Product'), ('B', 'Brand')], max_length=255)),
                ('Record_ID', models.TextField()),
                ('Datensatztyp', models.TextField()),
                ('Kampagnen_ID', models.TextField()),
                ('Kampagne_Kampagnename', models.TextField()),
                ('Tagesbudget_der_Kampagne', models.TextField()),
                ('Portfolio_ID', models.TextField()),
                ('Kampagnenstartdatum', models.TextField()),
                ('Kampagnenenddatum', models.TextField()),
                ('Kampagnentargetingtyp', models.TextField()),
                ('Anzeigengruppe', models.TextField()),
                ('Max_Gebot', models.TextField()),
                ('Keyword_oder_Produkt_Targeting', models.TextField()),
                ('Produkt_Targeting_ID', models.TextField()),
                ('Ubereinstimmungstyp', models.TextField()),
                ('SKU', models.TextField()),
                ('Kampagnenstatus', models.TextField()),
                ('Status_der_Anzeigengruppe', models.TextField()),
                ('Status', models.TextField()),
                ('Impressions', models.TextField()),
                ('Klicks', models.TextField()),
                ('Ausgaben', models.TextField()),
                ('Bestellungen', models.TextField()),
                ('Einheiten_insgesamt', models.TextField()),
                ('Verkäufe', models.TextField()),
                ('ACOS', models.TextField()),
                ('Gebotsstrategie', models.TextField()),
                ('Platzierungstyp', models.TextField()),
                ('Erhohung_von_Geboten_nach_Platzierung', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_products', to='dashboard.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
