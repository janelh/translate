import os, sys, subprocess, json
from os import path
from gtts import gTTS
from socket import *

# Open json config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Receiving
host = config['receiving']['host']
port = config['receiving']['port']
buffer = config['receiving']['buffer']

# Text to speech
mp3Filename = config['text_to_speech']['mp3_filename']

def main():
    # Wait for translation
    address = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(address)
    print("Waiting to receive messages...")
    while True:
        (data, address) = UDPSock.recvfrom(buffer)
        translatedText = data.decode('utf-8')
        print("Received text: " + translatedText)
        translatedTextToSpeech(translatedText)
    UDPSock.close()
    os._exit(0)

def translatedTextToSpeech(text):
    tts = gTTS(text=text, lang='en')
    tts.save(mp3Filename)
    if sys.platform == 'win32':
        os.startfile(mp3Filename)
    else:
        subprocess.call(["xdg-open", mp3Filename])


main()