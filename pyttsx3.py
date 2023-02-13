import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Establece la voz en español

text = "Hola, esto es una prueba de texto a voz"
engine.say(text)
engine.runAndWait()
