from datetime import datetime
def date_conversion(date_str):
    date_object=datetime.strptime(date_str,'%Y-%m-%d').date()
    return date_object









