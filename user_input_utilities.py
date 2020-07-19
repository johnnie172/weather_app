

def choose_diffrent_city(params):

    answer = input('the current city is {}, would you like to choose another city? (enter "YES" or the city name): '.format(params['query']))
    if answer.lower() != 'yes':
        params['query'] = str(answer.title())

    return params
