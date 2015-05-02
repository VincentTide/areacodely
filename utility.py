from dateutil.parser import parse
import datetime

DEFAULT_DATE = datetime.datetime(1901, 1, 1)

def parse_no_default(datestring):
    date = parse(datestring, default=DEFAULT_DATE)
    if date == DEFAULT_DATE:
        return None
    else:
        return date
