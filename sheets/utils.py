

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