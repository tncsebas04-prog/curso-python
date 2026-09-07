

import requests
from datetime import datetime , timezone, timedelta
from config import API_KEY


def consultar_clima(ciudad):
    url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {"q": ciudad, "appid": API_KEY, "units": "metric", "lang": "es"}
    respuesta = requests.get(url, params=parametros)
    if respuesta.status_code != 200:
        return "No he podido consultar el tiempo de esa ciudad."
    datos = respuesta.json()
    temperatura = datos["main"]["temp"]
    sensacion_termica = datos["main"]["feels_like"]
    clima = datos["weather"][0]["description"]
    ciudad_confirmada = datos["name"]
    desfase = datos["timezone"]
    hora_utc = datetime.now(timezone.utc)
    hora_local = hora_utc + timedelta(seconds=desfase)
    hora_texto = hora_local.strftime("%d/%m/%Y a las %H:%M")

    return f"En {ciudad_confirmada} hay {round(temperatura, 1)}°C, sensación de {round(sensacion_termica, 1)}°C, {clima}, la hora es {hora_texto}."

