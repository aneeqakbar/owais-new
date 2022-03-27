import datetime

def get_index_or_none(list, i, empty_value=None):
    try:
        if str(list[i]) == "nan":
            return empty_value
        return list[i]
    except:
        return empty_value


def get_percent_or_none(percent, value, empty_value=None):
    try:
        return ((float(percent) / 100) * float(value)) + float(value)
    except:
        return empty_value


def str_to_date(date_string, empty_value=None):
    try:
        year = str(date_string).split('.')[0][0:4]
        month = str(date_string).split('.')[0][4:6]
        day = str(date_string).split('.')[0][6:8]
        return datetime.datetime(year=int(year), month=int(month), day=int(day))
    except:
        return empty_value
    
def new_or_previous(new_value, previous_value):
    """If there is new value then return new value else previous_value"""
    if new_value:
        return new_value
    return previous_value