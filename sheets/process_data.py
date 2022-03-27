from random import randint
import pandas as pd
from sheets.utils import get_index_or_none, get_percent_or_none, str_to_date
from dashboard.models import AnalyticalValue, DataProduct, DataBrand
from django.core.paginator import Paginator
import datetime


# sheet_name1 = "Sponsored Brands-Kampagnen"
# sheet_name2 = "Sponsored Products-Kampagnen"

class ProcessSheetData():
    def __init__(self, file_path, type, client):
        self.file = file_path
        self.client = client
        self.type = type
        self.sheet = ""

        if self.type == "P":
            self.sheet = "Sponsored Products Campaigns"
        elif self.type == "B":
            self.sheet = "Sponsored Brands Campaigns"

    def process_data(self, commit=True):
            data = pd.read_excel(self.file, sheet_name=self.sheet)
            if commit:
                if self.type == "P":
                    self.commit_product_data(data)
                elif self.type == "B":
                    self.commit_brand_data(data)
                return True
            else:
                return data

    def commit_product_data(self, dataframe):

        Product = dataframe.get("Product", None)
        Entity = dataframe.get("Entity", None)
        Operation = dataframe.get("Operation", None)
        Campaign_Id = dataframe.get("Campaign Id", None)
        Ad_Group_Id = dataframe.get("Ad Group Id", None)
        Portfolio_Id = dataframe.get("Portfolio Id", None)
        Ad_Id = dataframe.get("Ad Id (Read only)", None)
        Keyword_Id = dataframe.get("Keyword Id (Read only)", None)
        Product_Targeting_Id = dataframe.get("Product Targeting Id (Read only)", None)
        Campaign_Name = dataframe.get("Campaign Name", None)
        Ad_Group_Name = dataframe.get("Ad Group Name", None)
        Start_Date = dataframe.get("Start Date", None)
        End_Date = dataframe.get("End Date", None)
        Targeting_Type = dataframe.get("Targeting Type", None)
        State = dataframe.get("State", None)
        Daily_Budget = dataframe.get("Daily Budget", None)
        SKU = dataframe.get("SKU", None)
        ASIN = dataframe.get("ASIN", None)
        Ad_Group_Default_Bid = dataframe.get("Ad Group Default Bid", None)
        Bid = dataframe.get("Bid", None)
        Keyword_Text = dataframe.get("Keyword Text", None)
        Match_Type = dataframe.get("Match Type", None)
        Bidding_Strategy = dataframe.get("Bidding Strategy", None)
        Placement = dataframe.get("Placement", None)
        placementProductPage = dataframe.get("placementProductPage", None)
        placementTop = dataframe.get("placementTop", None)
        Percentage = dataframe.get("Percentage", None)
        Product_Targeting_Expression = dataframe.get("Product Targeting Expression", None)
        Impressions = dataframe.get("Impressions", None)
        Clicks = dataframe.get("Clicks", None)
        Click_through_Rate = dataframe.get("Click-through Rate", None)
        Spend = dataframe.get("Spend", None)
        Sales = dataframe.get("Sales", None)
        Orders = dataframe.get("Orders", None)
        Units = dataframe.get("Units", None)
        Conversion_Rate = dataframe.get("Conversion Rate", None)
        Acos = dataframe.get("Acos", None)
        CPC = dataframe.get("CPC", None)
        ROAS = dataframe.get("ROAS", None)
        Campaign_Name_info_only = dataframe.get("Campaign Name (Informational only)", None)
        Ad_Group_Name_info_only = dataframe.get("Ad Group Name (Informational only)", None)
        Campaign_State_info_only = dataframe.get("Campaign State (Informational only)", None)
        Ad_Group_State_info_only = dataframe.get("Ad Group State (Informational only)", None)
        Ad_Group_Default_Bid_info_only = dataframe.get("Ad Group Default Bid (Informational only)", None)
        Resolved_Product_Targeting_Expression_info_only = dataframe.get("Resolved Product Targeting Expression (Informational only)", None)

        data_instances_created = []
        data_instances_exists = []
        analytical_values_created = []
        analytical_values_exists = []

        placementProductPage = get_index_or_none(Percentage, 1, None)
        placementTop = get_index_or_none(Percentage, 2, None)

        # for i in range(len(data)):
        current_campaign_id = ""
        current_Campaign_Name = ""
        current_Ad_Group_Name = ""
        current_Start_Date = ""
        current_End_Date = ""
        current_Targeting_Type = ""
        current_State = ""
        current_Daily_Budget = ""
        current_SKU = ""
        current_ASIN = ""
        current_Ad_Group_Default_Bid = ""
        current_Bidding_Strategy = ""
        # for i in range(100):
        for i in range(len(dataframe)):
            if get_index_or_none(Campaign_Id, i, None):
                current_campaign_id = get_index_or_none(Campaign_Id, i, None)
            if get_index_or_none(Campaign_Name, i, None):
                current_Campaign_Name = get_index_or_none(Campaign_Name, i, None)
            if get_index_or_none(Ad_Group_Name, i, None):
                current_Ad_Group_Name = get_index_or_none(Ad_Group_Name, i, None)
            if get_index_or_none(Start_Date, i, None):
                current_Start_Date = get_index_or_none(Start_Date, i, None)
            if get_index_or_none(End_Date, i, None):
                current_End_Date = get_index_or_none(End_Date, i, None)
            if get_index_or_none(Targeting_Type, i, None):
                current_Targeting_Type = get_index_or_none(Targeting_Type, i, None)
            if get_index_or_none(State, i, None):
                current_State = get_index_or_none(State, i, None)
            if get_index_or_none(Daily_Budget, i, None):
                current_Daily_Budget = get_index_or_none(Daily_Budget, i, None)
            if get_index_or_none(SKU, i, None):
                current_SKU = get_index_or_none(SKU, i, None)
            if get_index_or_none(ASIN, i, None):
                current_ASIN = get_index_or_none(ASIN, i, None)
            if get_index_or_none(Ad_Group_Default_Bid, i, None):
                current_Ad_Group_Default_Bid = get_index_or_none(Ad_Group_Default_Bid, i, None)
            if get_index_or_none(Bidding_Strategy, i, None):
                current_Bidding_Strategy = get_index_or_none(Bidding_Strategy, i, None)

            current_Ad_Id = get_index_or_none(Ad_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)

            if (current_Ad_Id or current_Keyword_Id or current_Product_Targeting_Id) and current_campaign_id:

                data_created = True
                try:
                    data = DataProduct.objects.get(
                        client = self.client,
                        Entity = current_Entity,
                        Campaign_Id = current_campaign_id,
                        Ad_Id = current_Ad_Id,
                        Keyword_Id = current_Keyword_Id,
                        Product_Targeting_Id = current_Product_Targeting_Id,
                        sheet_name = self.sheet,
                    )
                    data_created = False
                except:
                    data = DataProduct(
                        client = self.client,
                        Campaign_Id = current_campaign_id,
                        Ad_Id = current_Ad_Id,
                        Keyword_Id = current_Keyword_Id,
                        Product_Targeting_Id = current_Product_Targeting_Id,
                        sheet_name = self.sheet,
                    )

                data.type = self.type
                # data.created_at = datetime.datetime.now()-datetime.timedelta(days=8)
                data.Product = get_index_or_none(Product, i, None)
                data.Entity = get_index_or_none(Entity, i, None)
                data.Operation = get_index_or_none(Operation, i, None)
                data.Ad_Group_Id = get_index_or_none(Ad_Group_Id, i, None)
                data.Portfolio_Id = get_index_or_none(Portfolio_Id, i, None)
                data.Campaign_Name = current_Campaign_Name
                data.Ad_Group_Name = current_Ad_Group_Name
                data.Start_Date = str_to_date(current_Start_Date, None)
                data.End_Date = str_to_date(current_End_Date, None)
                data.Targeting_Type = current_Targeting_Type
                data.State = current_State
                data.Daily_Budget = current_Daily_Budget
                data.SKU = current_SKU
                data.ASIN = current_ASIN
                data.Ad_Group_Default_Bid = current_Ad_Group_Default_Bid
                data.Bid = get_percent_or_none(placementProductPage, get_index_or_none(Bid, i, None), None)
                data.Keyword_Text = get_index_or_none(Keyword_Text, i, None)
                data.Match_Type = get_index_or_none(Match_Type, i, None)
                data.Bidding_Strategy = current_Bidding_Strategy
                data.Placement = get_index_or_none(Placement, i, None)
                data.placementProductPage = placementProductPage
                data.placementTop = placementTop
                data.Percentage = get_index_or_none(Percentage, i, None)
                data.Product_Targeting_Expression = get_index_or_none(Product_Targeting_Expression, i, None)
                data.Campaign_Name_info_only = get_index_or_none(Campaign_Name_info_only, i, None)
                data.Ad_Group_Name_info_only = get_index_or_none(Ad_Group_Name_info_only, i, None)
                data.Campaign_State_info_only = get_index_or_none(Campaign_State_info_only, i, None)
                data.Ad_Group_State_info_only = get_index_or_none(Ad_Group_State_info_only, i, None)
                data.Ad_Group_Default_Bid_info_only = get_index_or_none(Ad_Group_Default_Bid_info_only, i, None)
                data.Resolved_Product_Targeting_Expression_info_only = get_index_or_none(Resolved_Product_Targeting_Expression_info_only, i, None)

                if data_created:
                    data_instances_created.append(data)
                else:
                    data_instances_exists.append(data)

        DataProduct.objects.bulk_create(data_instances_created)
        DataProduct.objects.bulk_update(data_instances_exists, fields=[
            "Product",
            "Entity",
            "Operation",
            "Campaign_Id",
            "Ad_Group_Id",
            "Portfolio_Id",
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
            "Campaign_Name",
            "Ad_Group_Name",
            "Campaign_State_info_only",
            "Ad_Group_State_info_only",
            "Ad_Group_Default_Bid_info_only",
            "Resolved_Product_Targeting_Expression_info_only",
        ])

        # for i in range(100):
        for i in range(len(dataframe)):
            current_campaign_id = ""
            if get_index_or_none(Campaign_Id, i, None):
                current_campaign_id = get_index_or_none(Campaign_Id, i, None)

            current_Ad_Id = get_index_or_none(Ad_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            # Campaign Name	Ad Group Name	Start Date	End Date	Targeting Type

            if (current_Ad_Id or current_Keyword_Id or current_Product_Targeting_Id) and current_campaign_id:
                values_created = True
                data = DataProduct.objects.get(
                    client = self.client,
                    Entity = current_Entity,
                    Campaign_Id = current_campaign_id,
                    Ad_Id = current_Ad_Id,
                    Keyword_Id = current_Keyword_Id,
                    Product_Targeting_Id = current_Product_Targeting_Id,
                    sheet_name = self.sheet,
                )

                # try:
                #     analytical_value = AnalyticalValue.objects.filter(
                #         type = self.type,
                #         data_product = data,
                #     ).order_by("-created_at").first()

                #     delta = datetime.timedelta(days=1)
                #     current_time = datetime.datetime.now()

                #     if not analytical_value:
                #         raise Exception("values does not exists")
                #     if int(current_time.timestamp()) - int(analytical_value.created_at.timestamp()) > int(delta.total_seconds()):
                #         raise Exception("values are of previous day")
                #     values_created = False
                # except:
                analytical_value = AnalyticalValue(
                    type = self.type,
                    data_product = data,
                    created_at = datetime.datetime.now()-datetime.timedelta(days=8)
                )
                    # created_at = datetime.datetime.now()

                analytical_value.data_product = data
                analytical_value.Impressions = get_index_or_none(Impressions, i, None)
                analytical_value.Clicks = get_index_or_none(Clicks, i, None)
                analytical_value.Click_through_Rate = get_index_or_none(Click_through_Rate, i, None)
                analytical_value.Spend = get_index_or_none(Spend, i, None)
                analytical_value.Sales = get_index_or_none(Sales, i, None)
                analytical_value.Orders = get_index_or_none(Orders, i, None)
                analytical_value.Units = get_index_or_none(Units, i, None)
                analytical_value.Conversion_Rate = get_index_or_none(Conversion_Rate, i, None)
                analytical_value.Acos = get_index_or_none(Acos, i, None)
                analytical_value.CPC = get_index_or_none(CPC, i, None)
                analytical_value.ROAS = get_index_or_none(ROAS, i, None)

                if values_created:
                    analytical_values_created.append(analytical_value)
                else:
                    analytical_values_exists.append(analytical_value)

        AnalyticalValue.objects.bulk_update(analytical_values_exists, fields=[
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
        ])
        AnalyticalValue.objects.bulk_create(analytical_values_created)

    def commit_brand_data(self, data):

        Record_ID = data.get("Record ID", None)
        Datensatztyp = data.get("Datensatztyp", None)
        Kampagnen_ID = data.get("Kampagnen-ID", None)
        Kampagne_Kampagnename = data.get("Kampagne:Kampagnename", None)
        Kampagnentyp = data.get("Kampagnentyp", None)
        Anzeigenformat = data.get("Anzeigenformat", None)
        Budget = data.get("Budget", None)
        Portfolio_ID = data.get("Portfolio-ID", None)
        Kampagnenstartdatum = data.get("Kampagnenstartdatum", None)
        Kampagnenenddatum = data.get("Kampagnenenddatum", None)
        Budget_Typ = data.get("Budget-Typ", None)
        URL_der_Landing_Page = data.get("URL der Landing Page", None)
        Landing_Page_ASINs = data.get("Landing Page-ASINs", None)
        Markenname = data.get("Markenname", None)
        Markenidentitäts_ID = data.get("Markenidentitäts-ID", None)
        Markenlogo_Asset_ID = data.get("Markenlogo-Asset-ID", None)
        Headline = data.get("Headline", None)
        Anzeigendesign_ASINs = data.get("Anzeigendesign ASINs", None)
        Medien_ID = data.get("Medien-ID", None)
        Automatisierte_Gebote = data.get("Automatisierte Gebote", None)
        Gebotsfaktor = data.get("Gebotsfaktor", None)
        Anzeigengruppe = data.get("Anzeigengruppe", None)
        Max_Gebot = data.get("Max. Gebot", None)
        Keyword = data.get("Keyword", None)
        Ubereinstimmungstyp = data.get("Übereinstimmungstyp", None)
        Kampagnenstatus = data.get("Kampagnenstatus", None)
        Bereitstellungsstatus = data.get("Bereitstellungsstatus", None)
        Status_der_Anzeigengruppe = data.get("Status der Anzeigengruppe", None)
        Status = data.get("Status", None)
        Impressions = data.get("Impressions", None)
        Klicks = data.get("Klicks", None)
        Ausgaben = data.get("Ausgaben", None)
        Bestellungen = data.get("Bestellungen", None)
        Einheiten_insgesamt = data.get("Einheiten insgesamt", None)
        Verkäufe = data.get("Verkäufe", None)
        ACOS = data.get("ACOS", None)
        Platzierungstyp = data.get("Platzierungstyp", None)

        # for i in range(1000):
        data_instances_created = []
        data_instances_exists = []
        for i in range(len(data)):
            created = True
            try:
                data = DataBrand.objects.get(
                    client = self.client,
                    Record_ID = get_index_or_none(Record_ID, i, ""),
                    Kampagnen_ID = get_index_or_none(Kampagnen_ID, i, ""),
                    type = self.type,
                    sheet_name = self.sheet,
                )
                created = False
            except:
                data = DataBrand(
                    client = self.client,
                    Record_ID = get_index_or_none(Record_ID, i, ""),
                    Kampagnen_ID = get_index_or_none(Kampagnen_ID, i, ""),
                    type = self.type,
                    sheet_name = self.sheet,
                )

            data.Datensatztyp = get_index_or_none(Datensatztyp, i, "")
            data.Kampagne_Kampagnename = get_index_or_none(Kampagne_Kampagnename, i, "")
            data.Kampagnentyp = get_index_or_none(Kampagnentyp, i, "")
            data.Anzeigenformat = get_index_or_none(Anzeigenformat, i, "")
            data.Budget = get_index_or_none(Budget, i, "")
            data.Portfolio_ID = get_index_or_none(Portfolio_ID, i, "")
            data.Kampagnenstartdatum = get_index_or_none(Kampagnenstartdatum, i, "")
            data.Kampagnenenddatum = get_index_or_none(Kampagnenenddatum, i, "")
            data.Budget_Typ = get_index_or_none(Budget_Typ, i, "")
            data.URL_der_Landing_Page = get_index_or_none(URL_der_Landing_Page, i, "")
            data.Landing_Page_ASINs = get_index_or_none(Landing_Page_ASINs, i, "")
            data.Markenname = get_index_or_none(Markenname, i, "")
            data.Markenidentitäts_ID = get_index_or_none(Markenidentitäts_ID, i, "")
            data.Markenlogo_Asset_ID = get_index_or_none(Markenlogo_Asset_ID, i, "")
            data.Headline = get_index_or_none(Headline, i, "")
            data.Anzeigendesign_ASINs = get_index_or_none(Anzeigendesign_ASINs, i, "")
            data.Medien_ID = get_index_or_none(Medien_ID, i, "")
            data.Automatisierte_Gebote = get_index_or_none(Automatisierte_Gebote, i, "")
            data.Gebotsfaktor = get_index_or_none(Gebotsfaktor, i, "")
            data.Anzeigengruppe = get_index_or_none(Anzeigengruppe, i, "")
            data.Max_Gebot = get_index_or_none(Max_Gebot, i, "")
            data.Keyword = get_index_or_none(Keyword, i, "")
            data.Ubereinstimmungstyp = get_index_or_none(Ubereinstimmungstyp, i, "")
            data.Kampagnenstatus = get_index_or_none(Kampagnenstatus, i, "")
            data.Bereitstellungsstatus = get_index_or_none(Bereitstellungsstatus, i, "")
            data.Status_der_Anzeigengruppe = get_index_or_none(Status_der_Anzeigengruppe, i, "")
            data.Status = get_index_or_none(Status, i, "")
            data.Impressions = get_index_or_none(Impressions, i, "")
            data.Klicks = get_index_or_none(Klicks, i, "")
            data.Ausgaben = get_index_or_none(Ausgaben, i, "")
            data.Bestellungen = get_index_or_none(Bestellungen, i, "")
            data.Einheiten_insgesamt = get_index_or_none(Einheiten_insgesamt, i, "")
            data.Verkäufe = get_index_or_none(Verkäufe, i, "")
            data.ACOS = get_index_or_none(ACOS, i, "")
            data.Platzierungstyp = get_index_or_none(Platzierungstyp, i, "")
            # data.save()
            if created:
                data_instances_created.append(data)
            else:
                data_instances_exists.append(data)
        DataBrand.objects.bulk_create(data_instances_created)
        DataBrand.objects.bulk_update(data_instances_exists, fields=[
            "Datensatztyp",
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
        ])