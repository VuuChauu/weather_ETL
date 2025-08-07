import requests
import json
from datetime import datetime
import pandas as pd
def fetch_weather_data(api_key, cities_file = "config/cities.json"):
    with open (cities_file, "r") as f:
        cities = json.load(f)
    data =[]
    for item in cities:
        city = item["city"]
        country = item["country"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
        res = requests.get(url)
        if res.status_code != 200:
            print("Không lấy được dữ liệu!")
            continue
        weather = res.json()
        data.append({
            "city": city,
            "country": country,
            "temperature": weather["main"]["temp"],
            "humidity": weather["main"]["humidity"],
            "weather": weather["weather"][0]["main"],
            "timestamp": datetime.utcnow()
        })
    return pd.DataFrame(data)

