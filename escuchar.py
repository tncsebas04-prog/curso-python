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
        audio = reconocedor.listen(fuente, timeout=5)


        

    try:
        return reconocedor.recognize_google(audio, language="es-CO").lower()
    except sr.UnknownValueError:
        print("No te he entendido.")
        return None
    except sr.RequestError:
        print("Error de conexión.")
        return None



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
            
        elif "hola" in texto:
            hablar("hola como te encuentas el dia de hoy")

    
        elif "adiós" in texto or "hasta luego" in texto:
            hablar("hasta luego")
            break
        else:
            hablar("No conozco esa orden.")
              
     


