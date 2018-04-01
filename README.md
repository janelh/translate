# Python Voice Translator

The idea for this project appeared following Spanish lessons one evening. My girlfriend was becoming annoyed at me constantly practising Spanish conversation with her. She has no idea what I am saying and she does't care what colour the cat is or how well I can count to ten.

To alleviate relationship strain, I dreamt of a future with a raspberry pi, a headset and a speaker duct taped to my shoulder. I would speak Spanish into the headset, the pi would translate and output the translations through the speaker. I have both a headset and a pi, however I have no usb speaker. As an improvisation, I thought instead that my translation could boom out through her computer speakers in the lounge room. Now, she can completely understand when I'm asking what the time is and where the bathroom located.

For some more technical details, there are two python scripts, the client and the server. The client script records the voice to a WAV file, transcripts the voice to text using Google Speech Translation. The text is then translated with the Googletrans python module, and the translated text is transferred to another computer with speakers. The server script on the other computer converts the received text to mp3, and opens the mp3 file.


## Getting Started

Add the client.py and config.json file to the raspberry pi, or computer that will receive your microphone voice input. Add the server.py and config.json to the computer that will receive the translated text and will output the translated audio file. 

### Prerequisites

Supports linux/windows and python3.

You will need to install the following python modules:

* pyaudio
* wave
* json
* SpeechRecognition
* Googletrans
* gTTS


### Running
Firstly, run the client.py script on the receiving computer. The receiving computer will wait to receive the translated text. On the sending computer, run the server.py script and indicate how many seconds to voice record. For example, to record for five seconds run the following command:

python client.py 5

When the script starts, you it will indicate when it starts and stops recording.

After you have recorded the audio, the receiving computer will output the text received and then open the default program you use to open mp3s.

## Future Development

I would like to add voice control to edit the options. The options available would be the record time and language destination/source (i.e. English to Spanish). I'd like generate the output audio on the client script instead of the server script. Finally, I'd like create another version with a single script which outputs through a pi usb speaker (duct taped to my shoulder).