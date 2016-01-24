#!/usr/bin/env python3

import speech_recognition as sr
import urllib
import httplib
import json
# obtain path to "test.wav" in the same folder as this script
import os
from os import path
import crud


# WAV Encoding function
def wav(filePath, name):
    newName = name + ".wav"
    os.system("ffmpeg -i " + filePath + " " + newName)
    return newName

def formatEntry(id, counter):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Feedbacks/' + id, '', {
           "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
           "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
         })
    # testObj = connection.getresponse().read()
    result = json.loads(connection.getresponse().read().decode("utf-8"))
    url = result["audioFile"]["url"]
    uuid = "temp" + str(counter + 1) + ".m4a"
    urllib.urlretrieve (url, uuid)
    newPath = wav(uuid, ("temp" + str(counter + 1)))
    nla = speech2Text(newPath)
    crud.put(id, {"reviewText" : nla})
    os.remove(uuid)
    os.remove(newPath)


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
        return r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
    except sr.UnknownValueError:
        return("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        return("Could not request results from IBM Speech to Text service; {0}".format(e))
