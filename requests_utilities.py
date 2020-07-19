import urllib

import requests
import consts

location = None


def test_internet_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        print(consts.INTERNET_CONNECTION_OK_MESSEGE)
        return True
    except:
        print(consts.INTERNET_CONNECTION_FAIL_MESSEGE)
        return False


def user_location(params):

    response = requests.get(consts.WEB_FOR_CITY)
    data = response.json()
    city = data['city']
    params["query"] = city

    return params


def weather_by_location_json(params):

    api_result = requests.get(consts.WEB_FOR_WEATHER, params)
    api_response = api_result.json()

    return api_response


def get_info_from_json(api_response, val_dict):

    location = api_response['location']
    val_dict['city_name'] = location['name']
    val_dict['local_time'] = location['localtime']

    current = api_response['current']
    val_dict['current_temp'] = current['temperature']
    val_dict['currnet_desc'] = current['weather_descriptions']
    val_dict['current_humidity'] = current['humidity']
    val_dict['current_visibility'] = current['visibility']

    return val_dict


def visibility_scale_to_desc(val_dict):

    current_visibility_dict = {
        0 : 'Dense fog', 1 : 'Thick fog',
        2 : 'Fog', 3 : 'Moderate fog',
        4 : 'Mist or thin fog', 5 : 'Poor',
        6 : 'Moderate', 7 : 'Good',
        8 : 'Very good', 9 : 'Exceptional', 10 : 'Exceptional'
    }
    key = val_dict['current_visibility']
    val_dict['current_visibility'] = current_visibility_dict[key]
    return val_dict


def change_desc_to_alphabet_only(val_dict):

    new_desc = ""
    for letter in val_dict['currnet_desc']:
        if letter.isalpha():
            new_desc += letter

    val_dict['currnet_desc'] = new_desc

    return val_dict


def make_string_for_weather(val_dict):

    time = val_dict['local_time']
    city = val_dict['city_name']
    desc = val_dict['currnet_desc']
    temp = val_dict['current_temp']
    hum = val_dict['current_humidity']
    vis = val_dict['current_visibility']

    return print("now {} at {} the weather is {}. \ntemp is {}°C, humidity: {}% and the visibility is {}."\
        .format(time, city, desc, temp, hum, vis))

