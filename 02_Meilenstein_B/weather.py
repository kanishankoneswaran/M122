import requests

API_KEY = "38c055954fd778d52684a3075a05afba"
# Variable für den API-Key
city = input("Willkommen! Bitte gib deine gewünschte Stadt ein.")
# Begrüssung vom Skript und Aufforderung eine Stadt einzugeben

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
# Die URL vom API-Wetterdienst
data = requests.get(url).json()
# Daten von der URL holen
temp = data['main']['temp']
humidity = data['main']['humidity']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
# Variablen für die Temperatur, Luftfeuchtigkeit, Höchsttemperatur und die niedrigste Temperatur


print(f'In {city} beträgt die Temperatur {temp} Grad. Die Luftfeuchtigkeit beträgt {humidity} Prozent. Die Höchsttemperatur liegt bei {temp_max} Grad und die niedrigste Temperatur bei {temp_min} Grad.')
# Ausgabesatz vom Skript mit den nötigen Informationen