import matplotlib.pyplot as plt
import requests

response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=a78417d484364aa29e674700252103&q=liepaja&days=4&aqi=yes&alerts=yes")

data = response.json()

#for forecast in data["current"]["last_updated"]["time"]:
#    print(forecast)

print(data["forecast"]["forecastday"][0]["day"]["maxtemp_c"])

fig, ax = plt.subplots()

days = ['day 1', 'day 2', 'day 3', 'day 4']
counts = []
