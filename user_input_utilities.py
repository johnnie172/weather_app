

def choose_diffrent_city(city):

    answer = input('the current city is {}, would you like to choose another city? (enter "NO" or the city name): '.format(city))
    if answer.lower() != 'no':
        city = str(answer.title())

    return city
