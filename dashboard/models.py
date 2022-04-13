from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from itertools import chain 
from django.utils import timezone

from dashboard.utils import calculate_change, get_number

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} -> {self.name}"

    @property
    def get_all_data(self):
        return list(chain(self.data_brands.all(), self.data_products.all()))

SHEET_CHOICES = (
    ("P", "product"),
    ("B", "brand"),
)

class AnalyticalValue(models.Model):
    data_product = models.ForeignKey("dashboard.DataProduct", on_delete=models.CASCADE, related_name="analytical_values", null=True, blank=True)
    data_brand = models.ForeignKey("dashboard.DataBrand", on_delete=models.CASCADE, related_name="analytical_values", null=True, blank=True)
    type = models.CharField(max_length=255, choices=SHEET_CHOICES)
    Impressions = models.TextField(null=True, blank=True)
    Clicks = models.TextField(null=True, blank=True)
    Click_through_Rate = models.TextField(null=True, blank=True)
    Spend = models.TextField(null=True, blank=True)
    Sales = models.TextField(null=True, blank=True)
    Orders = models.TextField(null=True, blank=True)
    Units = models.TextField(null=True, blank=True)
    Conversion_Rate = models.TextField(null=True, blank=True)
    Acos = models.TextField(null=True, blank=True)
    CPC = models.TextField(null=True, blank=True)
    ROAS = models.TextField(null=True, blank=True)
    Bid = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False, default=datetime.now())

    def __str__(self):
        if self.type == "P":
            return f"Data #{self.data_product.id} values -> #{self.id}"
        else:
            return f"Data #{self.data_brand.id} values -> #{self.id}"

    @property
    def get_data_model(self):
        if self.type == "P":
            return self.data_product
        else:
            return self.data_brand

class DataProduct(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="data_products")
    sheet_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=SHEET_CHOICES)
    Product = models.TextField(null=True, blank=True)
    Campaign_Id = models.TextField(null=True, blank=True)
    Entity = models.TextField(null=True, blank=True)
    Operation = models.TextField(null=True, blank=True)
    Ad_Group_Id = models.TextField(null=True, blank=True)
    Portfolio_Id = models.TextField(null=True, blank=True)
    Ad_Id = models.TextField(null=True, blank=True)
    Keyword_Id = models.TextField(null=True, blank=True)
    Product_Targeting_Id = models.TextField(null=True, blank=True)
    Campaign_Name = models.TextField(null=True, blank=True)
    Ad_Group_Name = models.TextField(null=True, blank=True)
    Start_Date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    End_Date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    Targeting_Type = models.TextField(null=True, blank=True)
    State = models.TextField(null=True, blank=True)
    Daily_Budget = models.TextField(null=True, blank=True)
    SKU = models.TextField(null=True, blank=True)
    ASIN = models.TextField(null=True, blank=True)
    Ad_Group_Default_Bid = models.TextField(null=True, blank=True)
    Bid = models.TextField(null=True, blank=True)
    Keyword_Text = models.TextField(null=True, blank=True)
    Match_Type = models.TextField(null=True, blank=True)
    Bidding_Strategy = models.TextField(null=True, blank=True)
    Placement = models.TextField(null=True, blank=True)
    placementProductPage = models.TextField(null=True, blank=True)
    placementTop = models.TextField(null=True, blank=True)
    Percentage = models.TextField(null=True, blank=True)
    Product_Targeting_Expression = models.TextField(null=True, blank=True)
    Campaign_Name_info_only = models.TextField(null=True, blank=True)
    Ad_Group_Name_info_only = models.TextField(null=True, blank=True)
    Campaign_State_info_only = models.TextField(null=True, blank=True)
    Ad_Group_State_info_only = models.TextField(null=True, blank=True)
    Ad_Group_Default_Bid_info_only = models.TextField(null=True, blank=True)
    Resolved_Product_Targeting_Expression_info_only = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False, default=datetime.now())

    def __str__(self):
        return f"{self.client.name}'s Product Data #{self.id}"

    @property
    def get_unique_id(self):
        if self.Product_Targeting_Id:
            return self.Product_Targeting_Id
        elif self.Product_Targeting_Expression:
            return self.Product_Targeting_Expression

    def get_field_analytics(self, field_name=''):
        fields = ['Impressions', 'Clicks', 'Click_through_Rate', 'Spend', 'Sales', 'Orders', 'Units', 'Conversion_Rate', 'Acos', 'CPC', 'ROAS', 'Bid']
        if not field_name or not field_name in fields:
            return {
                "daily": 0,
                "weekly": 0,
                "yearly": 0,
            }

        current_time = datetime.now()

        min_delta = timedelta(days=365)
        max_delta = timedelta(days=365*2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)

        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            yearly = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            yearly = 0

        min_delta = timedelta(weeks=1)
        max_delta = timedelta(weeks=2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)

        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            weekly = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            weekly = 0

        min_delta = timedelta(days=1)
        max_delta = timedelta(days=2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)
        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            daily = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            daily = 0

        return {
            "daily": daily,
            "weekly": weekly,
            "yearly": yearly,
        }

    def get_chart_data(self, field_name="", days=7):
        fields = ['Impressions', 'Clicks', 'Click_through_Rate', 'Spend', 'Sales', 'Orders', 'Units', 'Conversion_Rate', 'Acos', 'CPC', 'ROAS']
        if not field_name or not field_name in fields:
            return {
                "labels": [],
                "data": []
            }

        chart_data = {
            "labels": [],
            "data": []
        }

        current_time = datetime.now()
        analytical_values = self.analytical_values.all()
        indexes = int(days)
        for i in range(indexes):
            max_delta = current_time - timedelta(days=(indexes-1)-i)
            min_delta = current_time - timedelta(days=(indexes-1)-i+1)
            values = analytical_values.filter(created_at__range = [min_delta, max_delta]).values_list(field_name, flat=True)
            sum = 0
            for value in values:
                sum += float(get_number(value))
            chart_data['data'].append(f'{sum}')
            chart_data['labels'].append(f'Day {i+1}')
        return chart_data


class DataBrand(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="data_brands")
    sheet_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=SHEET_CHOICES)
    Product = models.TextField(null=True, blank=True)
    Entity = models.TextField(null=True, blank=True)
    Operation = models.TextField(null=True, blank=True)
    Campaign_Id = models.TextField(null=True, blank=True)
    Draft_Campaign_Id = models.TextField(null=True, blank=True)
    Portfolio_Id = models.TextField(null=True, blank=True)
    Ad_Group_Id = models.TextField(null=True, blank=True)
    Keyword_Id = models.TextField(null=True, blank=True)
    Product_Targeting_Id = models.TextField(null=True, blank=True)
    Campaign_Name = models.TextField(null=True, blank=True)
    Start_Date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    End_Date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    State = models.TextField(null=True, blank=True)
    Campaign_Serving_Status = models.TextField(null=True, blank=True)
    Budget_Type = models.TextField(null=True, blank=True)
    Budget = models.TextField(null=True, blank=True)
    Bid_Optimization = models.TextField(null=True, blank=True)
    Bid_Multiplier = models.TextField(null=True, blank=True)
    Bid = models.TextField(null=True, blank=True)
    Keyword_Text = models.TextField(null=True, blank=True)
    Match_Type = models.TextField(null=True, blank=True)
    Product_Targeting_Expression = models.TextField(null=True, blank=True)
    Ad_Format = models.TextField(null=True, blank=True)
    Landing_Page_URL = models.TextField(null=True, blank=True)
    Landing_Page_Asins = models.TextField(null=True, blank=True)
    Brand_Entity_Id = models.TextField(null=True, blank=True)
    Brand_Name = models.TextField(null=True, blank=True)
    Brand_Logo_Asset_Id = models.TextField(null=True, blank=True)
    Brand_Logo_URL = models.TextField(null=True, blank=True)
    Creative_Headline = models.TextField(null=True, blank=True)
    Creative_ASINs = models.TextField(null=True, blank=True)
    Video_Media_Ids = models.TextField(null=True, blank=True)
    Creative_Type = models.TextField(null=True, blank=True)
    Campaign_Name = models.TextField(null=True, blank=True)
    Campaign_State = models.TextField(null=True, blank=True)
    Resolved_Product_Targeting_Expression = models.TextField(null=True, blank=True)
    Landing_Page_Type = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False, default=datetime.now())

    def __str__(self):
        return f"{self.client.name}'s Product Data #{self.id}"

    @property
    def get_unique_id(self):
        if self.Product_Targeting_Id:
            return self.Product_Targeting_Id
        elif self.Product_Targeting_Expression:
            return self.Product_Targeting_Expression

    def get_field_analytics(self, field_name=''):
        fields = ['Impressions', 'Clicks', 'Click_through_Rate', 'Spend', 'Sales', 'Orders', 'Units', 'Conversion_Rate', 'Acos', 'CPC', 'ROAS', 'Bid']
        if not field_name or not field_name in fields:
            return {
                "daily": 0,
                "weekly": 0,
                "yearly": 0,
            }

        current_time = datetime.now()

        min_delta = timedelta(days=365)
        max_delta = timedelta(days=365*2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)

        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            yearly = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            yearly = 0

        min_delta = timedelta(weeks=1)
        max_delta = timedelta(weeks=2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)

        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            weekly = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            weekly = 0

        min_delta = timedelta(days=1)
        max_delta = timedelta(days=2)
        previous_datas = self.analytical_values.filter(created_at__range = [current_time - max_delta, current_time - min_delta]).values_list(field_name, flat=True)
        current_datas = self.analytical_values.filter(created_at__range = [current_time - min_delta, current_time]).values_list(field_name, flat=True)
        previous_value = 0
        for value in previous_datas:
            previous_value += float(get_number(value))
        current_value = 0
        for value in current_datas:
            current_value += float(get_number(value))
        try:
            previous_value = previous_value / len(previous_datas)
            current_value = current_value / len(current_datas)
            daily = calculate_change(current_value, previous_value)
        except ZeroDivisionError:
            daily = 0

        return {
            "daily": daily,
            "weekly": weekly,
            "yearly": yearly,
        }

    def get_chart_data(self, field_name="", days=7):
        fields = ['Impressions', 'Clicks', 'Click_through_Rate', 'Spend', 'Sales', 'Orders', 'Units', 'Conversion_Rate', 'Acos', 'CPC', 'ROAS']
        if not field_name or not field_name in fields:
            return {
                "labels": [],
                "data": []
            }

        chart_data = {
            "labels": [],
            "data": []
        }

        current_time = datetime.now()
        analytical_values = self.analytical_values.all()
        indexes = int(days)
        for i in range(indexes):
            max_delta = current_time - timedelta(days=(indexes-1)-i)
            min_delta = current_time - timedelta(days=(indexes-1)-i+1)
            values = analytical_values.filter(created_at__range = [min_delta, max_delta]).values_list(field_name, flat=True)
            sum = 0
            for value in values:
                sum += float(get_number(value))
            chart_data['data'].append(f'{sum}')
            chart_data['labels'].append(f'Day {i+1}')
        return chart_data


# Product Sheet Fields
    # Product
    # Entity
    # Operation
    # Campaign Id
    # Ad Group Id
    # Portfolio Id
    # Ad Id (Read only)
    # Keyword Id (Read only)
    # Product Targeting Id (Read only)
    # Campaign Name
    # Ad Group Name
    # Start Date
    # End Date
    # Targeting Type
    # State
    # Daily Budget
    # SKU
    # ASIN
    # Ad Group Default Bid
    # Bid
    # Keyword Text
    # Match Type
    # Bidding Strategy
    # Placement
    # placementProductPage
    # placementTop
    # Percentage
    # Product Targeting Expression
    # Impressions
    # Clicks
    # Click-through Rate
    # Spend
    # Sales
    # Orders
    # Units
    # Conversion Rate
    # Acos
    # CPC
    # ROAS
    # Campaign Name (Informational only)
    # Ad Group Name (Informational only)
    # Campaign State (Informational only)
    # Ad Group State (Informational only)
    # Ad Group Default Bid (Informational only)
    # Resolved Product Targeting Expression (Informational only)

# ###################################################################
    # Product
    # Entity
    # Operation
    # Campaign_Id
    # Ad_Group_Id
    # Portfolio_Id
    # Ad_Id
    # Keyword_Id
    # Product_Targeting_Id
    # Campaign_Name
    # Ad_Group_Name
    # Start_Date
    # End_Date
    # Targeting_Type
    # State
    # Daily_Budget
    # SKU
    # ASIN
    # Ad_Group_Default_Bid
    # Bid
    # Keyword_Text
    # Match_Type
    # Bidding_Strategy
    # Placement
    # placementProductPage
    # placementTop
    # Percentage
    # Product_Targeting_Expression
    # Impressions
    # Clicks
    # Click_through_Rate
    # Spend
    # Sales
    # Orders
    # Units
    # Conversion_Rate
    # Acos
    # CPC
    # ROAS
    # Campaign_Name
    # Ad_Group_Name
    # Campaign_State
    # Ad_Group_State
    # Ad_Group_Default_Bid
    # Resolved_Product_Targeting_Expression























# Brand Sheet Fields
    # Record_ID
    # Datensatztyp
    # Kampagnen_ID
    # Kampagne_Kampagnename
    # Kampagnentyp
    # Anzeigenformat
    # Budget
    # Portfolio_ID
    # Kampagnenstartdatum
    # Kampagnenenddatum
    # Budget_Typ
    # URL_der_Landing_Page
    # Landing_Page_ASINs
    # Markenname
    # Markenidentitäts_ID
    # Markenlogo_Asset_ID
    # Headline
    # Anzeigendesign_ASINs
    # Medien_ID
    # Automatisierte_Gebote
    # Gebotsfaktor
    # Anzeigengruppe
    # Max_Gebot
    # Keyword
    # Übereinstimmungstyp
    # Kampagnenstatus
    # Bereitstellungsstatus
    # Status_der_Anzeigengruppe
    # Status
    # Impressions
    # Klicks
    # Ausgaben
    # Bestellungen
    # Einheiten_insgesamt
    # Verkäufe
    # ACOS
    # Platzierungstyp


