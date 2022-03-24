from django.contrib import admin
from django.db.models import Q

from dashboard.models import AnalyticalValue, DataProduct, DataBrand

# Register your models here.



@admin.register(DataProduct)
class DataProductAdmin(admin.ModelAdmin):
    search_fields = ("Ad_Id", "Keyword_Id", "Product_Targeting_Id")
    ordering = ['-created_at']
    list_display = (
        "client",
        "sheet_name",
        "type",
        "Product",
        "Entity",
        "Operation",
        "Ad_Group_Id",
        "Portfolio_Id",
        "Ad_Id",
        "Keyword_Id",
        "Product_Targeting_Id",
        "Campaign_Name",
        "Ad_Group_Name",
        "Start_Date",
        "End_Date",
        "Targeting_Type",
        "State",
        "Daily_Budget",
        "SKU",
        "ASIN",
        "Ad_Group_Default_Bid",
        "Bid",
        "Keyword_Text",
        "Match_Type",
        "Bidding_Strategy",
        "Placement",
        "placementProductPage",
        "placementTop",
        "Percentage",
        "Product_Targeting_Expression",
        "Campaign_Name_info_only",
        "Ad_Group_Name_info_only",
        "Campaign_State_info_only",
        "Ad_Group_State_info_only",
        "Ad_Group_Default_Bid_info_only",
        "Resolved_Product_Targeting_Expression_info_only",
        "created_at",
    )

@admin.register(AnalyticalValue)
class AnalyticalValueAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = (
        "data_product",
        "data_brand",
        "type",
        "get_unique_id",
        "Impressions",
        "Clicks",
        "Click_through_Rate",
        "Spend",
        "Sales",
        "Orders",
        "Units",
        "Conversion_Rate",
        "Acos",
        "CPC",
        "ROAS",
        "created_at",
    )

    def get_unique_id(self, obj):
        if obj.get_data_model.Ad_Id:
            return obj.get_data_model.Ad_Id
        elif obj.get_data_model.Keyword_Id:
            return obj.get_data_model.Keyword_Id
        elif obj.get_data_model.Product_Targeting_Id:
            return obj.get_data_model.Product_Targeting_Id

@admin.register(DataBrand)
class DataBrandAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "sheet_name",
        "type",
        "Record_ID",
        "Datensatztyp",
        "Kampagnen_ID",
        "Kampagne_Kampagnename",
        "Kampagnentyp",
        "Anzeigenformat",
        "Budget",
        "Portfolio_ID",
        "Kampagnenstartdatum",
        "Kampagnenenddatum",
        "Budget_Typ",
        "URL_der_Landing_Page",
        "Landing_Page_ASINs",
        "Markenname",
        "Markenidentitäts_ID",
        "Markenlogo_Asset_ID",
        "Headline",
        "Anzeigendesign_ASINs",
        "Medien_ID",
        "Automatisierte_Gebote",
        "Gebotsfaktor",
        "Anzeigengruppe",
        "Max_Gebot",
        "Keyword",
        "Ubereinstimmungstyp",
        "Kampagnenstatus",
        "Bereitstellungsstatus",
        "Status_der_Anzeigengruppe",
        "Status",
        "Impressions",
        "Klicks",
        "Ausgaben",
        "Bestellungen",
        "Einheiten_insgesamt",
        "Verkäufe",
        "ACOS",
        "Platzierungstyp",
        "created_at",
    )