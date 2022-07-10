# Meilenstein C

### Meine Vorgehensweise

Für das Projekt brauchte ich erstmal ein nutzbares API-Key von einem Wetterdienst, der sowas anbietet. Dabei bin ich auf openweathermap.org gestossen. Hier habe ich einen kostenlosen API-Key requestet. Bis der aktiviert wurde dauerte es noch ein paar Stunden. In der Zeit schrieb ich das Skript. Als aller erstes sollte das Skript einen Begrüssungssatz ausgeben, in dem man die gewünschte Stadt eingeben kann. Hier legte ich eine neue Variable mit dem Namen "City" an. Eine weitere Variable haben ich für die URL gemacht. Danach konnte ich die nötigen Variablen für die Temperatur, Luftfeuchtigkeit, Höchsttemperatur und für die niedrigste Temperatur machen.

Am Schluss schrieb ich noch einen Ausgabesatz mit den gefragten Informationen, die lautet: 
- In {city} beträgt die Temperatur {temp} Grad. Die Luftfeuchtigkeit beträgt {humidity} Prozent. Die Höchsttemperatur liegt bei {temp_max} Grad und die niedrigste Temperatur bei {temp_min} Grad.