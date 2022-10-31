from copy import error
import datetime
from datetime import date
def converter_data(data):
    d = data.split("-")
    print( int(d[0]), datetime.datetime.now().date().strftime("%Y"))
    if ((int(d[0])>1950) and (int(d[0])<=int(datetime.datetime.now().date().strftime("%Y"))) and (int(d[1])>0) and (int(d[1])<=12) and (int(d[2])>0) and (int(d[2])<=31)):

        return date(int(d[0]), int(d[1]), int(d[2]))
    else:
        return error

