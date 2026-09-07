import sys
import pyaudiowpatch as pyaudio
from tiempo import consultar_clima
import pyttsx3

sys.modules["pyaudio"] = pyaudio

import speech_recognition as sr


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
hablar("hable ahora")
texto = escuchar()

if texto:
    if "tiempo" in texto or "clima" in texto:
        hablar("por favor diga el nombre de su ciudad")
        ciudad = escuchar()
        if ciudad:
            hablar(consultar_clima(ciudad))
        else:
            hablar("no se nada al respecto de esa ciudad")

    elif "hola" in texto:
        hablar("Hola, ¿en qué te ayudo?")
    else:
        hablar("No conozco esa orden.")
              
     


