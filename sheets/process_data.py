from random import randint
import time
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

    def commit_product_data(self, dataframe, date=datetime.datetime.now()):

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
        data_instances = [None for i in range(len(dataframe))]
        analytical_values_created = []
        analytical_values_exists = []


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
        current_placementProductPage = ""
        current_placementTop = ""
        # for i in range(100):
        for i in range(len(dataframe)):
            placementProductPage = str(get_index_or_none(Percentage, i, ""))
            placementTop = str(get_index_or_none(Percentage, i+1, ""))
            if len(placementProductPage) > 0 and len(placementTop) > 0:
                current_placementProductPage = placementProductPage
                current_placementTop = placementTop

            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_campaign_id = _value
            _value = get_index_or_none(Campaign_Name, i, None)
            if _value:
                current_Campaign_Name = _value
            _value = get_index_or_none(Ad_Group_Name, i, None)
            if _value:
                current_Ad_Group_Name = _value
            _value = get_index_or_none(Start_Date, i, None)
            if _value:
                current_Start_Date = _value
            _value = get_index_or_none(End_Date, i, None)
            if _value:
                current_End_Date = _value
            _value = get_index_or_none(Targeting_Type, i, None)
            if _value:
                current_Targeting_Type = _value
            _value = get_index_or_none(State, i, None)
            if _value:
                current_State = _value
            _value = get_index_or_none(Daily_Budget, i, None)
            if _value:
                current_Daily_Budget = _value
            _value = get_index_or_none(SKU, i, None)
            if _value:
                current_SKU = _value
            _value = get_index_or_none(ASIN, i, None)
            if _value:
                current_ASIN = _value
            _value = get_index_or_none(Ad_Group_Default_Bid, i, None)
            if _value:
                current_Ad_Group_Default_Bid = _value
            _value = get_index_or_none(Bidding_Strategy, i, None)
            if _value:
                current_Bidding_Strategy = _value

            current_Ad_Id = get_index_or_none(Ad_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            # if "Negative" in current_Entity:
            #     print("is Negative")
            if (current_Ad_Id or current_Keyword_Id or current_Product_Targeting_Id)\
                and current_campaign_id and (not "Negative" in current_Entity):

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
                data.Bid = get_percent_or_none(current_placementProductPage, get_index_or_none(Bid, i, None), None)
                data.Keyword_Text = get_index_or_none(Keyword_Text, i, None)
                data.Match_Type = get_index_or_none(Match_Type, i, None)
                data.Bidding_Strategy = current_Bidding_Strategy
                data.Placement = get_index_or_none(Placement, i, None)
                data.placementProductPage = current_placementProductPage
                data.placementTop = current_placementTop
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
                # data_instances[i] = data
                print(f"data #{i}")

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
        # for i in range(len(dataframe)):
        delta_in_secs = datetime.timedelta(days=1).total_seconds()
        current_timestamp = int(datetime.datetime.now().timestamp())
        current_time = datetime.datetime.now()
        for i in range(len(dataframe)):
            current_campaign_id = ""
            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_campaign_id = _value

            current_Ad_Id = get_index_or_none(Ad_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            # Campaign Name Ad Group Name	Start Date	End Date	Targeting Type

            if (current_Ad_Id or current_Keyword_Id or current_Product_Targeting_Id)\
                and current_campaign_id and (not "Negative" in current_Entity):
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

                try:
                    analytical_value = AnalyticalValue.objects.filter(
                        type = self.type,
                        data_product = data,
                        created_at = date,
                    ).order_by("-created_at").first()

                    if not analytical_value:
                        raise Exception("values does not exists")
                    # if current_timestamp - int(analytical_value.created_at.timestamp()) > delta_in_secs:
                    #     raise Exception("values are of previous day")
                    values_created = False
                except:
                    analytical_value = AnalyticalValue(
                        type = self.type,
                        data_product = data,
                        created_at = date
                    )
                        # created_at = datetime.datetime.now()-datetime.timedelta(days=8)

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
                print(f"analytics #{i}")

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

    def commit_brand_data(self, dataframe):
        Product = dataframe.get("Product", None)
        Entity = dataframe.get("Entity", None)
        Operation = dataframe.get("Operation", None)
        Campaign_Id = dataframe.get("Campaign Id", None)
        Draft_Campaign_Id = dataframe.get("Draft Campaign Id", None)
        Portfolio_Id = dataframe.get("Portfolio Id", None)
        Ad_Group_Id = dataframe.get("Ad Group Id (Read only)", None)
        Keyword_Id = dataframe.get("Keyword Id (Read only)", None)
        Product_Targeting_Id = dataframe.get("Product Targeting Id (Read only)", None)
        Campaign_Name = dataframe.get("Campaign Name", None)
        Start_Date = dataframe.get("Start Date", None)
        End_Date = dataframe.get("End Date", None)
        State = dataframe.get("State", None)
        Budget_Type = dataframe.get("Budget Type", None)
        Budget = dataframe.get("Budget", None)
        Bid_Optimization = dataframe.get("Bid Optimization", None)
        Bid_Multiplier = dataframe.get("Bid Multiplier", None)
        Bid = dataframe.get("Bid", None)
        Keyword_Text = dataframe.get("Keyword Text", None)
        Match_Type = dataframe.get("Match Type", None)
        Product_Targeting_Expression = dataframe.get("Product Targeting Expression", None)
        Ad_Format = dataframe.get("Ad Format", None)
        Landing_Page_URL = dataframe.get("Landing Page URL", None)
        Landing_Page_Asins = dataframe.get("Landing Page Asins", None)
        Brand_Entity_Id = dataframe.get("Brand Entity Id", None)
        Brand_Name = dataframe.get("Brand Name", None)
        Brand_Logo_Asset_Id = dataframe.get("Brand Logo Asset Id", None)
        Brand_Logo_URL = dataframe.get("Brand Logo URL", None)
        Creative_Headline = dataframe.get("Creative Headline", None)
        Creative_ASINs = dataframe.get("Creative ASINs", None)
        Video_Media_Ids = dataframe.get("Video Media Ids", None)
        Creative_Type = dataframe.get("Creative Type", None)
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

        data_instances_created = []
        data_instances_exists = []
        data_instances = [None for i in range(len(dataframe))]
        analytical_values_created = []
        analytical_values_exists = []


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
            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_campaign_id = _value
            _value = get_index_or_none(Campaign_Name, i, None)
            if _value:
                current_Campaign_Name = _value
            _value = get_index_or_none(Ad_Group_Name, i, None)
            if _value:
                current_Ad_Group_Name = _value
            _value = get_index_or_none(Start_Date, i, None)
            if _value:
                current_Start_Date = _value
            _value = get_index_or_none(End_Date, i, None)
            if _value:
                current_End_Date = _value
            _value = get_index_or_none(Targeting_Type, i, None)
            if _value:
                current_Targeting_Type = _value
            _value = get_index_or_none(State, i, None)
            if _value:
                current_State = _value
            _value = get_index_or_none(Daily_Budget, i, None)
            if _value:
                current_Daily_Budget = _value
            _value = get_index_or_none(SKU, i, None)
            if _value:
                current_SKU = _value
            _value = get_index_or_none(ASIN, i, None)
            if _value:
                current_ASIN = _value
            _value = get_index_or_none(Ad_Group_Default_Bid, i, None)
            if _value:
                current_Ad_Group_Default_Bid = _value
            _value = get_index_or_none(Bidding_Strategy, i, None)
            if _value:
                current_Bidding_Strategy = _value

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
                Product
                Entity
                Operation
                Campaign_Id
                Draft_Campaign_Id
                Portfolio_Id
                Ad_Group_Id
                Keyword_Id
                Product_Targeting_Id
                Campaign_Name
                Start_Date
                End_Date
                State
                Budget_Type
                Budget
                Bid_Optimization
                Bid_Multiplier
                Bid
                Keyword_Text
                Match_Type
                Product_Targeting_Expression
                Ad_Format
                Landing_Page_URL
                Landing_Page_Asins
                Brand_Entity_Id
                Brand_Name
                Brand_Logo_Asset_Id
                Brand_Logo_URL
                Creative_Headline
                Creative_ASINs
                Video_Media_Ids
                Creative_Type

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
                data.Bid = get_percent_or_none(current_placementProductPage, get_index_or_none(Bid, i, None), None)
                data.Keyword_Text = get_index_or_none(Keyword_Text, i, None)
                data.Match_Type = get_index_or_none(Match_Type, i, None)
                data.Bidding_Strategy = current_Bidding_Strategy
                data.Placement = get_index_or_none(Placement, i, None)
                data.placementProductPage = current_placementProductPage
                data.placementTop = current_placementTop
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
                # data_instances[i] = data
                print(f"data #{i}")

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
        # for i in range(len(dataframe)):
        delta_in_secs = datetime.timedelta(days=1).total_seconds()
        current_timestamp = int(datetime.datetime.now().timestamp())
        current_time = datetime.datetime.now()
        for i in range(1000):
            current_campaign_id = ""
            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_campaign_id = _value

            current_Ad_Id = get_index_or_none(Ad_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            # Campaign Name Ad Group Name	Start Date	End Date	Targeting Type

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
                # data = data_instances[i]

                try:
                    analytical_value = AnalyticalValue.objects.filter(
                        type = self.type,
                        data_product = data,
                    ).order_by("-created_at").first()

                    if not analytical_value:
                        raise Exception("values does not exists")
                    if current_timestamp - int(analytical_value.created_at.timestamp()) > delta_in_secs:
                        raise Exception("values are of previous day")
                    values_created = False
                except:
                    analytical_value = AnalyticalValue(
                        type = self.type,
                        data_product = data,
                        created_at = current_time
                    )
                        # created_at = datetime.datetime.now()-datetime.timedelta(days=8)

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
                print(f"analytics #{i}")

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