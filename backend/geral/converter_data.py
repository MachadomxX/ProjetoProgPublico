from copy import error
import datetime
from datetime import date
def converter_data(data):
    d = data.split("-")
    try:
        return date(int(d[0]), int(d[1]), int(d[2]))
    except:
        return error

