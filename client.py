import json
import pyaudio
import wave
import speech_recognition as sr
import os
import sys, getopt
from os import path
from googletrans import Translator
from socket import *

# Open json config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Recording
channels = config['recording']['channels']
rate = config['recording']['rate']
chunk = config['recording']['chunk']
waveFilename = config['recording']['wave_filename']
wavePath = path.join(path.dirname(path.realpath(__file__)), waveFilename)

# Sending
host = config['sending']['host']
port = config['sending']['port']

def main(recordSeconds):
    recordInput(recordSeconds)
    text = inputToText()
    translatedText = translateText(text)
    send(translatedText)

def recordInput(recordSeconds):
    format = pyaudio.paInt16    
    audio = pyaudio.PyAudio()
    # Start recording
    stream = audio.open(format=format, channels=channels,
                    rate=rate, input=True,
                    frames_per_buffer=chunk)
    print("recording...")
    frames = []
    for i in range(0, int(rate / chunk * int(recordSeconds))):
        data = stream.read(chunk)
        frames.append(data)
    print("finished recording")
    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    # Save recording to wave file
    waveFile = wave.open(waveFilename, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def inputToText():
    r = sr.Recognizer()
    with sr.AudioFile(wavePath) as source:
        audio = r.record(source)
    # Recognize speech using Google Speech Recognition
    try:
        transcription = r.recognize_google(audio, language='es-ES')
        print("Google Speech Recognition thinks you said " + transcription)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return transcription

def translateText(text):
    translator = Translator()
    result = translator.translate(text, src='es', dest='en')
    return result.text

def send(translatedText):
    address = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.sendto(translatedText.encode('utf-8'), address)
    UDPSock.close()
    os._exit(0) 

main(sys.argv[1])