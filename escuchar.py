import sys
import pyaudiowpatch as pyaudio
sys.modules["pyaudio"] = pyaudio

import speech_recognition as sr
import pyttsx3
from datetime import datetime
from tiempo import consultar_clima

reconocedor = sr.Recognizer()


def hablar(texto):
    motor = pyttsx3.init()
    motor.say(texto)
    motor.runAndWait()


def escuchar():
    with sr.Microphone() as fuente:
        reconocedor.adjust_for_ambient_noise(fuente, duration=1)
        audio = reconocedor.listen(fuente)
    try:
        return reconocedor.recognize_google(audio, language="es-CO").lower()
    except sr.UnknownValueError:
        print("No te he entendido.")
        return None
    except sr.RequestError:
        print("Error de conexión.")
        return None


def decir_hora():
    ahora = datetime.now().strftime("%H:%M")
    hablar(f"Son las {ahora}")
def saludar2():
    hablar("excelente pasandola demasiado bien y dime en que puedo ayudarte")

def saludar():
    hablar("Hola, ¿cómo te encuentras hoy?")


comandos = {
    "hora": decir_hora,
    "hola": saludar,
    "bien": saludar2,
}

hablar("hola, ¿en qué puedo ayudarte?")

while True:
    texto = escuchar()
    if texto:
        if "tiempo" in texto or "clima" in texto:
            hablar("por favor diga el nombre de su ciudad")
            ciudad = escuchar()
            if ciudad:
                hablar(consultar_clima(ciudad))
            else:
                hablar("no conozco esa ciudad")
        elif "adiós" in texto or "hasta luego" in texto:
            hablar("hasta luego")
            break
        else:
            for palabra, funcion in comandos.items():
                if palabra in texto:
                    funcion()
                    break
            
              
     


