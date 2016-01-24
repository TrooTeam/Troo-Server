#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "test.wav" in the same folder as this script
from os import path


def speech2Text(filepath):
    WAV_FILE = path.join(path.dirname(path.realpath(__file__)), filepath)
    # use "test.wav" as the audio source
    r = sr.Recognizer()
    with sr.WavFile(WAV_FILE) as source:
        audio = r.record(source) # read the entire WAV file
    # recognize speech using IBM Speech to Text
    IBM_USERNAME = "e4600454-7958-42db-868a-8dcc50491f2c" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "Kz2jCk6s5Lo0" # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))
