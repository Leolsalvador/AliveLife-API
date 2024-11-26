from datetime import date, datetime

def format_date(date_value):
    if isinstance(date_value, (date, datetime)):
        return date_value.strftime('%d/%m/%Y')
    return date_value 