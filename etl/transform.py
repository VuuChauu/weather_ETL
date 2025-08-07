def clean_weather_data(df):
    df = df.dropna()
    df["city"] = df["city"].str.title()
    return df
