# test_local.py
from etl.extract import fetch_weather_data
from etl.transform import clean_weather_data
from etl.load import upload_to_bigquery

df = fetch_weather_data("e80e73135ab81e6a14600ea4474772c4")
df_clean = clean_weather_data(df)
upload_to_bigquery(df_clean, "weather-468210.weather_dataset.weather_data")
