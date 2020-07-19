import requests_utilities
import user_input_utilities

val_dict = {}

params = {
    'access_key': 'e4eb60681cb3f243e72cafc0fd07df97',
    'query': 'new york'
}

if __name__ == '__main__':
    requests_utilities.test_internet_connection()
    params = requests_utilities.user_location(params)
    user_input_utilities.choose_diffrent_city(params)
    api_response = requests_utilities.weather_by_location_json(params)
    val_dict = requests_utilities.get_info_from_json(api_response, val_dict)
    val_dict = requests_utilities.change_desc_to_alphabet_only(val_dict)
    val_dict = requests_utilities.visibility_scale_to_desc(val_dict)
    requests_utilities.make_string_for_weather(val_dict)
