import os
import requests
import os
key = os.environ['KEY']
def get_data_city(key:str, city:str)->dict:
    url = f'https://api.openweathermap.org/data/2.5/weather'
    
    payload = {
        'q':city,
        'appid':key
    }
    
    r = requests.get(url,params=payload)
    return r.json()

# print(get_data_city(key,"samarkand"))

