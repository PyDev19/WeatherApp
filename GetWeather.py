import FormatResponse
import requests
import App


def get_weather(city):
    weather_key = 'f81531c787785da7aba874a6b746f65c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    App.label['text'] = FormatResponse.format_response(weather)
