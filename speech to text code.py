#speech-to-text code in Python using the SpeechRecognition library:

import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Open the microphone and start recording
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Use the recognizer to convert speech to text
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand your speech")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
