import pandas as pd
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'  
api_key = '5fb8dbf07e74d88defa8132b0f668746'.strip()
cities = ['Mumbai','London','New York','Tokyo','Sydney']

data_list = []

for city in cities:
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    r = requests.get(url, params=params)
    data = r.json()
    
    # Check if request was successful
    if r.status_code == 200 and 'main' in data:
        data_list.append({
            'City': city,
            'Temperature (C)': data['main']['temp'],
            'Weather': data['weather'][0]['description'],
            'Humidity (%)': data['main']['humidity'],
            'Wind Speed (m/s)': data['wind']['speed']
        })
    else:
        print(f"Skipping {city}, reason: {data.get('message', 'Unknown error')}")

df = pd.DataFrame(data_list)
print(df)
df.to_csv('weather_data.csv', index=False)