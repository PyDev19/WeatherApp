def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        tempmin = weather['main']['temp_min']
        tempmax = weather['main']['temp_max']
        feelslike = weather['main']['feels_like']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        windspeed = weather['wind']['speed']
        winddeg = weather['wind']['deg']
        visibility = weather['visibility']

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s \nMin Temperature (°C): %s \nMax ' \
                    'Temperature (°C): %s \nFeels Like (°C): %s \nHumidity : %s%% \nPressure: %s mb \nWind Speed: %s ' \
                    'meter/sec \nWind Degree: %s° \nVisibility: %s meters' % (
                        name, country, desc, temp, tempmin, tempmax, feelslike, humidity, pressure, windspeed, winddeg,
                        visibility)
    except:
        final_str = 'There was a problem retrieving that\ninfo.\n\nPlease enter city name again or zip\ncode again.'

    return final_str