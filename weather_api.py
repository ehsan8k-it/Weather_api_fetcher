import requests
# api key you can generate from openweathermap.org
api_key = "Your api keys comes here"

# Latitude AND longitude of your area You can get it from gpt or Google
lat = 28.96395
lon = 69.06849
city = "Zain koh loti"

# This is api url of whether forcast
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# getting data from url
res = requests.get(url)
# Converting that data into readable JSON formate.
data = res.json()
weather_description = data["weather"][0]["description"]

print(f"The weather of {city} is: {weather_description}")

