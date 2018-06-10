''' Homework 10 - DSC 20, SP18'''


def workaround(x):
    """this function exists to let okpy accept submissions. (DO NOT MODIFY)
    >>> workaround(5)
    10
    """
    return x * 2

##############################################################################
# Problem - JSON
##############################################################################
import json
from datetime import datetime


def clean_json(json, keys_list):
    "*** YOUR CODE HERE ***"
    for wea in json['forecast']:
        for key in keys_list:
            del wea[key]


def farenheight_to_celsius(json):
    "*** YOUR CODE HERE ***"
    diff = 32
    numer = 5.0
    denom = 9.0
    for wea in json['forecast']:
        wea['high'] = str(round(((float(wea['high'])) - diff) * numer / denom))
        wea['low'] = str(round(((float(wea['low'])) - diff) * numer / denom))


def reformat_date(json):
    "*** YOUR CODE HERE ***"
    for wea in json['forecast']:
        datetime_object = datetime.strptime(wea['date'], '%d %b %Y')
        wea['date'] = datetime_object.strftime('%d.%m.%Y')


def add_temp_diff(json):
    "*** YOUR CODE HERE ***"
    for wea in json['forecast']:
        wea['temp_range'] = str(abs(int(wea['high']) - int(wea['low'])))


def largest_temp_diff(json):
    "*** YOUR CODE HERE ***"
    checker = 0
    date = None
    for obj in json['forecast']:
        if float(obj['temp_range']) > checker:
            checker = float(obj['temp_range'])
            date = obj['date']
    return date


def save_json_file(fname, data):
    "*** YOUR CODE HERE ***"
    with open(fname, 'w') as outfile:
        json.dump(data, outfile, indent = 2)

def do_problem():
    '''Wrapper that uses your utility methods above to accomplish tasks.'''
    "*** YOUR CODE HERE ***"
    with open('weather.json') as weather:
        wea_data = json.load(weather)
    clean_json(wea_data, ['code', 'text'])
    farenheight_to_celsius(wea_data)
    reformat_date(wea_data)
    add_temp_diff(wea_data)
    wea_data['largest_drop'] = largest_temp_diff(wea_data)
    save_json_file('new_temps.json', wea_data)
