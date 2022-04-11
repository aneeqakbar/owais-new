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
        # data_instances = [None for i in range(len(dataframe))]
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

        print(f"saving and updating data")
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
        DataProduct.objects.bulk_create(data_instances_created)
        # for i in range(len(dataframe)):
        # delta_in_secs = datetime.timedelta(days=1).total_seconds()
        # current_timestamp = int(datetime.datetime.now().timestamp())
        # current_time = datetime.datetime.now()
        print(f"saving and updating of data done")
        current_campaign_id = ""
        for i in range(len(dataframe)):
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

        print(f"saving and updating of anlytical data")
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
        print(f"saving and updating of anlytical data done")

    def commit_brand_data(self, dataframe, date=datetime.datetime.now()):
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
        Campaign_Serving_Status = dataframe.get("Campaign Serving Status (Informational only)", None)
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
        Campaign_State = dataframe.get("Campaign State (Informational only)", None)
        Resolved_Product_Targeting_Expression = dataframe.get("Resolved Product Targeting Expression (Informational only)", None)
        Landing_Page_Type = dataframe.get("Landing Page Type (Informational only)", None)

        data_instances_created = []
        data_instances_exists = []
        analytical_values_created = []
        analytical_values_exists = []

        current_Campaign_Id = ""
        current_Draft_Campaign_Id = ""
        current_Portfolio_Id = ""
        current_Ad_Group_Id = ""
        current_Keyword_Id = ""
        current_Product_Targeting_Id = ""
        current_Start_Date = None
        current_End_Date = None
        current_Budget_Type = ""
        current_Budget = ""
        current_Bid_Optimization = ""
        current_Bid_Multiplier = ""
        current_Ad_Format = ""
        current_Landing_Page_URL = ""
        current_Landing_Page_Asins = ""
        current_Brand_Entity_Id = ""
        current_Brand_Name = ""
        current_Brand_Logo_Asset_Id = ""
        current_Brand_Logo_URL = ""
        current_Creative_Headline = ""
        current_Creative_ASINs = ""
        current_Video_Media_Ids = ""
        current_Creative_Type = ""
        current_Entity = ""

        # for i in range(100):
        for i in range(len(dataframe)):
            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_Campaign_Id = _value
            _value = get_index_or_none(Start_Date, i, None)
            if _value:
                current_Start_Date = _value
            _value = get_index_or_none(End_Date, i, None)
            if _value:
                current_End_Date = _value
            _value = get_index_or_none(Budget_Type, i, None)
            if _value:
                current_Budget_Type = _value
            _value = get_index_or_none(Budget, i, None)
            if _value:
                current_Budget = _value
            _value = get_index_or_none(Bid_Optimization, i, None)
            if _value:
                current_Bid_Optimization = _value
            _value = get_index_or_none(Bid_Multiplier, i, None)
            if _value:
                current_Bid_Multiplier = _value
            _value = get_index_or_none(Ad_Format, i, None)
            if _value:
                current_Ad_Format = _value
            _value = get_index_or_none(Landing_Page_URL, i, None)
            if _value:
                current_Landing_Page_URL = _value
            _value = get_index_or_none(Landing_Page_Asins, i, None)
            if _value:
                current_Landing_Page_Asins = _value
            _value = get_index_or_none(Brand_Entity_Id, i, None)
            if _value:
                current_Brand_Entity_Id = _value
            _value = get_index_or_none(Brand_Name, i, None)
            if _value:
                current_Brand_Name = _value
            _value = get_index_or_none(Brand_Logo_Asset_Id, i, None)
            if _value:
                current_Brand_Logo_Asset_Id = _value
            _value = get_index_or_none(Brand_Logo_URL, i, None)
            if _value:
                current_Brand_Logo_URL = _value
            _value = get_index_or_none(Creative_Headline, i, None)
            if _value:
                current_Creative_Headline = _value
            _value = get_index_or_none(Creative_ASINs, i, None)
            if _value:
                current_Creative_ASINs = _value
            _value = get_index_or_none(Video_Media_Ids, i, None)
            if _value:
                current_Video_Media_Ids = _value
            _value = get_index_or_none(Creative_Type, i, None)
            if _value:
                current_Creative_Type = _value

            current_Ad_Group_Id = get_index_or_none(current_Ad_Group_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            current_Draft_Campaign_Id = get_index_or_none(Draft_Campaign_Id, i, None)
            current_Portfolio_Id = get_index_or_none(Portfolio_Id, i, None)

            if (current_Ad_Group_Id or current_Keyword_Id or current_Product_Targeting_Id or current_Entity or current_Draft_Campaign_Id or current_Portfolio_Id) and current_Campaign_Id:

                data_created = True
                try:
                    data = DataBrand.objects.get(
                        client = self.client,
                        Entity = current_Entity,
                        Campaign_Id = current_Campaign_Id,
                        Draft_Campaign_Id = current_Draft_Campaign_Id,
                        Portfolio_Id = current_Portfolio_Id,
                        Ad_Group_Id = current_Ad_Group_Id,
                        Keyword_Id = current_Keyword_Id,
                        Product_Targeting_Id = current_Product_Targeting_Id,
                        sheet_name = self.sheet,
                    )
                    data_created = False
                except:
                    data = DataBrand(
                        client = self.client,
                        Entity = current_Entity,
                        Campaign_Id = current_Campaign_Id,
                        Draft_Campaign_Id = current_Draft_Campaign_Id,
                        Portfolio_Id = current_Portfolio_Id,
                        Ad_Group_Id = current_Ad_Group_Id,
                        Keyword_Id = current_Keyword_Id,
                        Product_Targeting_Id = current_Product_Targeting_Id,
                        sheet_name = self.sheet,
                    )

                data.type = self.type
                # data.created_at = datetime.datetime.now()-datetime.timedelta(days=8)
                data.Product = get_index_or_none(Product, i, None)
                data.Entity = get_index_or_none(Entity, i, None)
                data.Operation = get_index_or_none(Operation, i, None)
                data.Campaign_Name = get_index_or_none(Campaign_Name, i, None)
                data.Start_Date = str_to_date(current_Start_Date, None)
                data.End_Date = str_to_date(current_End_Date, None)
                data.State = get_index_or_none(State, i, None)
                data.Budget_Type = current_Budget_Type
                data.Budget = current_Budget
                data.Bid_Optimization = current_Bid_Optimization
                data.Bid_Multiplier = current_Bid_Multiplier
                data.Bid = get_index_or_none(Bid, i, None)
                data.Keyword_Text = get_index_or_none(Keyword_Text, i, None)
                data.Match_Type = get_index_or_none(Match_Type, i, None)
                data.Product_Targeting_Expression = get_index_or_none(Product_Targeting_Expression, i, None)
                data.Ad_Format = current_Ad_Format
                data.Landing_Page_URL = current_Landing_Page_URL
                data.Landing_Page_Asins = current_Landing_Page_Asins
                data.Brand_Entity_Id = current_Brand_Entity_Id
                data.Brand_Name = current_Brand_Name
                data.Brand_Logo_Asset_Id = current_Brand_Logo_Asset_Id
                data.Brand_Logo_URL = current_Brand_Logo_URL
                data.Creative_Headline = current_Creative_Headline
                data.Creative_ASINs = current_Creative_ASINs
                data.Video_Media_Ids = current_Video_Media_Ids
                data.Creative_Type = current_Creative_Type

                if data_created:
                    data_instances_created.append(data)
                else:
                    data_instances_exists.append(data)
                # data_instances[i] = data
                print(f"data #{i}")

        DataBrand.objects.bulk_create(data_instances_created)
        DataBrand.objects.bulk_update(data_instances_exists, fields=[
            "Product",
            "Entity",
            "Operation",
            "Campaign_Id",
            "Draft_Campaign_Id",
            "Portfolio_Id",
            "Ad_Group_Id",
            "Keyword_Id",
            "Product_Targeting_Id",
            "Campaign_Name",
            "Start_Date",
            "End_Date",
            "State",
            "Budget_Type",
            "Budget",
            "Bid_Optimization",
            "Bid_Multiplier",
            "Bid",
            "Keyword_Text",
            "Match_Type",
            "Product_Targeting_Expression",
            "Ad_Format",
            "Landing_Page_URL",
            "Landing_Page_Asins",
            "Brand_Entity_Id",
            "Brand_Name",
            "Brand_Logo_Asset_Id",
            "Brand_Logo_URL",
            "Creative_Headline",
            "Creative_ASINs",
            "Video_Media_Ids",
            "Creative_Type",
        ])
        # for i in range(len(dataframe)):
        # delta_in_secs = datetime.timedelta(days=1).total_seconds()
        # current_timestamp = int(datetime.datetime.now().timestamp())
        # current_time = datetime.datetime.now()

        current_Campaign_Id = ""
        current_Draft_Campaign_Id = ""
        current_Portfolio_Id = ""
        current_Ad_Group_Id = ""
        current_Keyword_Id = ""
        current_Product_Targeting_Id = ""
        current_Entity = ""
        # for i in range(100):
        for i in range(len(dataframe)):
            _value = get_index_or_none(Campaign_Id, i, None)
            if _value:
                current_Campaign_Id = _value
            _value = get_index_or_none(Draft_Campaign_Id, i, None)
            if _value:
                current_Draft_Campaign_Id = _value
            _value = get_index_or_none(Start_Date, i, None)
            if _value:
                current_Start_Date = _value
            _value = get_index_or_none(End_Date, i, None)
            if _value:
                current_End_Date = _value

            current_Ad_Group_Id = get_index_or_none(current_Ad_Group_Id, i, None)
            current_Keyword_Id = get_index_or_none(Keyword_Id, i, None)
            current_Product_Targeting_Id = get_index_or_none(Product_Targeting_Id, i, None)
            current_Entity = get_index_or_none(Entity, i, None)
            current_Draft_Campaign_Id = get_index_or_none(Draft_Campaign_Id, i, None)
            current_Portfolio_Id = get_index_or_none(Portfolio_Id, i, None)

            if (current_Ad_Group_Id or current_Keyword_Id or current_Product_Targeting_Id or current_Entity or current_Draft_Campaign_Id or current_Portfolio_Id) and current_Campaign_Id:

                values_created = True
                data = DataBrand.objects.filter(
                    client = self.client,
                    Entity = current_Entity,
                    Campaign_Id = current_Campaign_Id,
                    Draft_Campaign_Id = current_Draft_Campaign_Id,
                    Portfolio_Id = current_Portfolio_Id,
                    Ad_Group_Id = current_Ad_Group_Id,
                    Keyword_Id = current_Keyword_Id,
                    Product_Targeting_Id = current_Product_Targeting_Id,
                    sheet_name = self.sheet,
                ).order_by("-id").first()

                analytical_value = None
                try:
                    analytical_value = AnalyticalValue.objects.get(
                        type = self.type,
                        data_brand = data,
                        created_at = date,
                    )
                    values_created = False
                except:
                    analytical_value = AnalyticalValue(
                        type = self.type,
                        data_brand = data,
                        created_at = date
                    )
                        # created_at = datetime.datetime.now()-datetime.timedelta(days=8)

                analytical_value.data_brand = data
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