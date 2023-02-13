from gtts import gTTS
import os

mytext = """¡Gracias por ver este video sobre liderazgo!."""
audio = gTTS(text=mytext, lang="es", slow=False)

audio.save("liderazgo10.mp3")
# os.system("start example.mp3")