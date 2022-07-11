#############################################################

#FileName:          weather.py

#Crated:            08.07.2022

#Last Edited:       10.07.2022

#Version:           v1.0

#Creater:           Kanishan Koneswaran

#Short-Description: Wetterdaten von Städten auswerten

#Language:          Python

#############################################################


import requests

# Variable für den API-Key - requested von openweathermap.org
API_KEY = "38c055954fd778d52684a3075a05afba"

# Begrüssung vom Skript und Aufforderung eine Stadt einzugeben - gewünschte Stadt als Variable festgelegt
city = input("Willkommen! Bitte gib deine gewünschte Stadt ein.")

# Die URL vom API-Wetterdienst - von hier nimmt ds Skript die nötigen Informationen wie Temperatur etc.
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

# Daten von der URL holen - .json bringt die Informationen in die richtige Form
data = requests.get(url).json()


# Variablen für die Temperatur, Luftfeuchtigkeit, Höchsttemperatur und die niedrigste Temperatur - Die Informationen werden von der API geholt und als Variable festgelegt
temp = data['main']['temp']
humidity = data['main']['humidity']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']


# Ausgabesatz vom Skript mit den nötigen Informationen - Das Skript gibt die verlangen Informaionen in vollständigen Sätzen aus. Hierfür werden die festgelegten Variabeln verwendet.
print(f'In {city} beträgt die Temperatur {temp} Grad. Die Luftfeuchtigkeit beträgt {humidity} Prozent. Die Höchsttemperatur liegt bei {temp_max} Grad und die niedrigste Temperatur bei {temp_min} Grad.')