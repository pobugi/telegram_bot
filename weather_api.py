import requests



def current_weather(city):

    url_base = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=05443b3ba2b770a860712cc4afb3a43e"
    url = url_base.format(city)

    bulk_data = requests.get(url).json()

    try:

        current_temperature = bulk_data['main']['temp']

        return 'Current temperature in {}: {} C'.format(city.capitalize(), current_temperature)
    except KeyError:
        return '{} city not found'.format(city)

