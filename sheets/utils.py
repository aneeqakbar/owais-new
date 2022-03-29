import datetime

def get_index_or_none(list, i, empty_value=None):
    try:
        value = list[i]
        if str(value) == "nan":
            return empty_value
        return value
    except:
        return empty_value


def get_percent_or_none(percent, value, empty_value=None):
    try:
        value = float(value)
        percent = float(percent)
        return ((percent / 100) * value) + value
    except:
        return empty_value


def str_to_date(date_string, empty_value=None):
    try:
        date_string = str(date_string).split('.')[0]
        year = date_string[0:4]
        month = date_string[4:6]
        day = date_string[6:8]
        return datetime.datetime(year=int(year), month=int(month), day=int(day))
    except:
        return empty_value
    
def new_or_previous(new_value, previous_value):
    """If there is new value then return new value else previous_value"""
    if new_value:
        return new_value
    return previous_value