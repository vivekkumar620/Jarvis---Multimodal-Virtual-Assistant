# Jarvis

J.A.R.V.I.S - A Multimodal Assistant
Created and Tested with Python 3.10
An attempt to make a very simple, Personal Assistant that understands speech as well as text input and is capable of performing tasks other than conversing. It also capture your face and match through image database then create a situation.

Converses, barely.
Talk to J.A.R.V.I.S : hello
J.A.R.V.I.S : Well, hello

Talk to J.A.R.V.I.S : Who is iron man?
J.A.R.V.I.S : Iron man is the one who created me.

Talk to J.A.R.V.I.S : What does JARVIS stand for?
J.A.R.V.I.S : JARVIS stands for Just A Rather Very Intelligent System

Talk to J.A.R.V.I.S : play music
J.A.R.V.I.S : On it!
Talk to J.A.R.V.I.S : play music
J.A.R.V.I.S : On it!
Talk to J.A.R.V.I.S : please open rhythmbox jarvis
J.A.R.V.I.S : Right away, sir!

Tells time.
Talk to J.A.R.V.I.S : what time is it?
J.A.R.V.I.S : The time is 4 43 am

Gives a brief system status.
Talk to J.A.R.V.I.S : how are you? / System report.
J.A.R.V.I.S : I am fine, sir. All systems are at 100 percent. Battery percentage: 100%. 

Suggests Googling for all unrecognized interrogative questions
Talk to J.A.R.V.I.S : What is IIT, Bombay?
J.A.R.V.I.S : Do you want me to google that for you?
Talk to J.A.R.V.I.S : yes
J.A.R.V.I.S : Right away, sir! Created new window in existing browser session.

Plays any song, first search result in youtube
Talk to J.A.R.V.I.S : play me a song
J.A.R.V.I.S : What song, sir?
Talk to J.A.R.V.I.S : Alter Bridge Isolation
J.A.R.V.I.S : On it! Created new window in existing browser session.

Uses youtube.py script to find the first search result for the last user input in above case, and opens it in chromium browser.

Searches internet.
Talk to J.A.R.V.I.S : Google what is the answer to life?
J.A.R.V.I.S : Right away, sir! Created new window in existing browser session.
Talk to J.A.R.V.I.S : Search youtube for Call of Duty
J.A.R.V.I.S : On it! Created new window in existing browser session.
Talk to J.A.R.V.I.S : Search for Navi Mumbai on google maps
J.A.R.V.I.S : On it! Created new window in existing browser session

Other:
Standard replies for unrecognized/unmatched inputs

Talk to J.A.R.V.I.S : you are dumb
J.A.R.V.I.S : I don't understand that yet. Maybe you could teach me.
Talk to J.A.R.V.I.S : no I won't
J.A.R.V.I.S : I don't know how to answer that. Maybe I could interest you in something else.

Talk to J.A.R.V.I.S : go to sleep / exit / quit / bye / goodbye

closes the python script.

Requirements:
Make sure you install these packages before moving forward to other python libraries-

You can run pip install -r requirements.txt to install them all.

Individual packages listed as follows-

 Face Recognition
pip install face_Recognition

date and time
pip install datetime

Speech Recognition
pip install SpeechRecognition

PyAudio is required for microphone input
pip install pyaudio

alsaaudio: (For Volume Control, Linux only)
pip install pyalsaaudio

ttsx: (Offline Text to Speech Service)
pip install pyttsx

Optional for Google Text to Speech :
gTTS: (Google Text to Speech service)
pip install gTTS
PyGame: (For audio playback with gTTS)

Installation:
Clone this repository. Change directories to go to that directory. Run the script "script.py" from the directory containing it. Run script as:

python script.py : for text mode (default) of input

python script.py --voice : for voice mode of input

python script.py --voice --gtts : for voice mode of input, with Google Text to Speech enabled.
