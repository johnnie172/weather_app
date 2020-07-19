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
    return city


def weather_by_location_json(params):

    api_result = requests.get(consts.WEB_FOR_WEATHER, params)
    api_response = api_result.json()
    print(api_response)
    return api_response


def get_info_from_json(api_response, weather_dict):

    location = api_response['location']
    weather_dict['city_name'] = location['name']
    weather_dict['local_time'] = location['localtime']

    current = api_response['current']
    weather_dict['current_temp'] = current['temperature']
    weather_dict['currnet_desc'] = current['weather_descriptions']
    weather_dict['current_humidity'] = current['humidity']
    weather_dict['current_visibility'] = current['visibility']

    return weather_dict

