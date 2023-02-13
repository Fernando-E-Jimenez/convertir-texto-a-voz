import json
import requests

url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/<instance_id>/v1/synthesize"

text = "Hola, esto es una prueba de texto a voz"

headers = {
    "Content-Type": "application/json",
    "Accept": "audio/mp3",
    "Authorization": "Bearer <api_key>"
}

payload = {
    "text": text,
    "voice": "es-ES_EnriqueVoice",
    "accept": "audio/mp3"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

with open("speech.mp3", "wb") as f:
    f.write(response.content)
