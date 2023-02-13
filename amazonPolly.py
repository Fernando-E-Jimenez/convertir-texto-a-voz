import boto3

client = boto3.client('polly', region_name='us-west-2')

text = "Hola, esto es una prueba de texto a voz"

response = client.synthesize_speech(
    VoiceId='Miguel',
    OutputFormat='mp3',
    Text=text,
    TextType='text'
)

with open("speech.mp3", "wb") as f:
    f.write(response['AudioStream'].read())
