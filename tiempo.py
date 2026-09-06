import requests
from config import API_KEY

ciudad = input("Ingrese el nombre de la ciudad: ")
url = "http://api.openweathermap.org/data/2.5/weather"
parametros = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}


respuesta = requests.get(url, params=parametros)
datos = respuesta.json()
temperatura = datos["main"]["temp"]
sensacion_termica = datos["main"]["feels_like"]
clima = datos["weather"][0]["description"]
ciudad_confirmada = datos["name"]

print(f"En {ciudad_confirmada} hay {round(temperatura, 1)}°C, sensación de {round(sensacion_termica, 1)}°C, {clima}.")
