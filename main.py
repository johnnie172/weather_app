import requests_utilities
import user_input_utilities
import utilities
import consts


weather_dict = {}

params = {
    'access_key': 'e4eb60681cb3f243e72cafc0fd07df97',
    'query': 'new york'
}

if __name__ == '__main__':

    if requests_utilities.check_for_internet_connection():
        print(consts.INTERNET_CONNECTION_OK_MESSEGE)
        params["query"] = requests_utilities.get_user_location()
        user_input_utilities.choose_diffrent_city(params)
        api_response = requests_utilities.weather_by_location_json(params)
        weather_dict = requests_utilities.get_info_from_json(api_response, weather_dict)
        weather_dict['current_desc'] = utilities.change_desc_to_alphabet_only(weather_dict['current_desc'])
        weather_dict = utilities.visibility_scale_to_desc(weather_dict)
        print(utilities.make_string_for_weather(weather_dict))
    else:
        print(consts.INTERNET_CONNECTION_FAIL_MESSEGE)