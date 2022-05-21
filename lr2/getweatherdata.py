import requests

api_key = "ключ" # api ключ 
url = "http://api.openweathermap.org/data/2.5/weather" # урл запроса

def get_weather_data(place, key=api_key):

    res = requests.get( # отправка запроса
        url,
        params = { # объвляение параметров
            "q": place,
            "appid": key,
            "units": "metric" # возвращать градусы в цельсиях
        }

    )

    return res.text # парсинг в текст и возврат из функции
    
    
if __name__ == "__main__":
    print(get_weather_data("Saint Petersburg"))
    print(get_weather_data("Chicago"))
    print(get_weather_data("Dhaka"))
