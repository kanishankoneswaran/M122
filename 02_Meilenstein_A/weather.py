import requests

API_KEY = "38c055954fd778d52684a3075a05afba"
city = input("Willkommen! Bitte gib deine gewünschte Stadt ein.")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']



print(f'In {city} beträgt die Temperatur {temp} Grad. Die Luftfeuchtigkeit beträgt {humidity} Prozent. Die Höchsttemperatur liegt bei {temp_max} Grad und die niedrigste Temperatur bei {temp_min} Grad.')