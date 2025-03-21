import requests

response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=a78417d484364aa29e674700252103&q=liepaja&days=1&aqi=yes&alerts=yes")

data = response.json()

for forecast in data["current"]["last_updated"]:
    print(forecast)

print(data)
