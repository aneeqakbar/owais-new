
import re


def calculate_change(new, old):
    return (new-old) / old *100




def get_number(value):
    number = re.sub("[^0-9.+-]", '', str(value))
    if number:
        return number
    return "0"








# month_labels = ["January", "Febuary","March", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# chart_data = {
#     "labels": month_labels,
#     "data": []
# }

# current_time = datetime.now()
# min_delta = timedelta(days=365)
# max_delta = timedelta(days=365*2)
# analytical_values = data.analytical_values.filter(created_at__range = [current_time - min_delta, current_time])
# indexes = 12
# for i in range(indexes):
#     values = analytical_values.filter(created_at__month = i + 1).values_list("Impressions", flat=True)
#     sum = 0
#     for value in values:
#         sum += int(value)
#     chart_data['data'].append(f'{sum}')



# indexes = 30
# for i in range(indexes):
#     current_time = datetime.datetime.now()
#     max_delta = current_time - datetime.timedelta(days=(indexes-1)-i)

#     analytical_value = AnalyticalValue(
#         type = self.type,
#         data_product = data,
#         created_at = max_delta
#     )
#         # created_at = datetime.datetime.now()-datetime.timedelta(days=8)

#     analytical_value.data_product = data
#     analytical_value.Impressions = float(get_index_or_none(Impressions, i, None)) + randint(0, 2000)
#     analytical_value.Clicks = get_index_or_none(Clicks, i, None)
#     analytical_value.Click_through_Rate = get_index_or_none(Click_through_Rate, i, None)
#     analytical_value.Spend = get_index_or_none(Spend, i, None)
#     analytical_value.Sales = get_index_or_none(Sales, i, None)
#     analytical_value.Orders = get_index_or_none(Orders, i, None)
#     analytical_value.Units = get_index_or_none(Units, i, None)
#     analytical_value.Conversion_Rate = get_index_or_none(Conversion_Rate, i, None)
#     analytical_value.Acos = get_index_or_none(Acos, i, None)
#     analytical_value.CPC = get_index_or_none(CPC, i, None)
#     analytical_value.ROAS = get_index_or_none(ROAS, i, None)
#     analytical_value.save()