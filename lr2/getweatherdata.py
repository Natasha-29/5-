import requests

api_key = "ключ" # api ключ 
url = "http://api.openweathermap.org/data/2.5/weather" # урл запроса

def get_weather_data(place, key=api_key):
    if place is None or place == '' or api_key is None or api_key == '':                      # проверка на пустые строки
        return None

    resp = requests.get(url)
    resp_json = json.loads(resp.content)                                                      # декодирование

    result_json = {
        "name": resp_json['name'],                                                            # Название города
        "coord": {
            "lon": resp_json['coord']['lon'],                                                 # долгота
            "lat": resp_json['coord']['lat']                                                  # широта
        },
        "country": resp_json['sys']['country'],                                               # код страны
        "feels_like": round((resp_json['main']['feels_like'] - 273.15), 2),                   # как ощущается температура с переводом в Цельсии и округлением 
        "timezone": "UTC%+d" % (resp_json['timezone'] / 3600)                                 # временая зона со сдвигом в часах
    }
    return json.dumps(result_json)
    
if __name__ == "__main__":
    print(get_weather_data("Saint Petersburg"))
    print(get_weather_data("Chicago"))
    print(get_weather_data("Dhaka"))
