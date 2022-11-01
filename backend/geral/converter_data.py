from copy import error
import datetime
from datetime import date
def converter_data(data):
    d = data.split("-")
    print( int(d[0]), datetime.datetime.now().date().strftime("%Y"))
    if date(int(d[0]), int(d[1]), int(d[2])) == error:
        return error
    else: 
        return date(int(d[0]), int(d[1]), int(d[2]))

