# Python/Rasberry Pi Voice Translator

This project was created as an aid to improve spanish skills using a battery powered portable rasberry pi with a usb microphone and a networked computer with speakers. When you speak spanish into the microphone, your voice will recorded and saved to a wave file. The wave audio will then be transcriped from voice to text with Google Speech Recognition. The transcribed text is translated from spanish to english, and the translated text is sent to the other computer on the network. The other computer will receive the translated text, convert the text to mp3 and then open this audio file.

## Getting Started

Update the config.json file with ip address of the translation text recieving computer, and update any other settings as required. Add the client.py and config.json file to the rasberry pi, or computer that will receive your microphone voice input. Add the server.py and config.json to the computer that will receive the translated text and will output the translated audio file. 

### Prerequisites

The translator supports both linux/windows oses and python3.

You will need to install the following python modules:

* pyaudio
* wave
* json
* SpeechRecognition
* Googletrans
* gTTS


### Running
Firstly, run the client.py script on the receiving computer. The receiving computer will wait to receive the translated text. On the sending computer, run the server.py script and indicate how many seconds to voice record. For example, to record for five seconds run the following command:

	**python client.py 5**

When the script starts, you it will indicate when it starts and stops recording.

After you have recorded the audio, the receiving computer will output the text receieved and then open the default program you use to open mp3s.


