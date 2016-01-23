import os
import sys
import logging
import json
import httplib
import urllib
import audiotranscode
import houndify
import string
import random
import wave
import time
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool

houndClient = houndify.StreamingHoundClient("F98d-lDRNRHV91T7LFIiKqHAZauzZbsvytojjNyFqr8sdZTl_9UmMjW4joxKqTJO7w688WUi7Cl1tRCjst3WRw==",
											"2z8RgKlFDs2paNd-opTnmQ==")
# spoof location
houndClient.setLocation(37.388309, -121.973968)
BUFFER_SIZE = 512

def wav(filePath, name):
	newName = name + '.wav'
	os.system("ffmpeg -i " + filePath + " " + newName)
	return newName

class MyListener(houndify.HoundListener):
	globalResponse = {}
	def onPartialTranscript(self, transcript):
		print "Partial transcript: " + transcript
	def onFinalResponse(self, response):
		print "Final response: " + str(response)

	def onTranslatedResponse(self, response):
		print "Translated response: " + response
	def onError(self, err):
		print "ERROR"

def post(params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Feedbacks', params, {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	})
	return connection.getresponse().read()

def put(params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('PUT', '/1/classes/Feedbacks/'+params, json.dumps({
		"tags": tags
     }), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()


def get(paramstring):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks', str(paramstring), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()


webapp = Flask(__name__)
@webapp.route("/")
def root():
	return ('App running.')

# API Routes
# General format is "/api/<endpoint here>"

# Sample of loading from Parse into a Dicti
# result = json.loads(connection.getresponse().read().decode("utf-8"))

@webapp.route("/api/create")
def create(newObj):
	data = request.method
	return post(data)
@webapp.route("/api/read")
def read():
	return get()

@webapp.route("/api/update/<id>")
def update(id):
	return put(id);

@webapp.route("/api/speech2text")
def speech2text():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks/vYGZor1rHD', '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	# testObj = connection.getresponse().read()
	result = json.loads(connection.getresponse().read().decode("utf-8"))
	url = result["audioFile"]["url"]
	unique = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
	uuid = unique + ".m4a"
	urllib.urlretrieve (url, uuid)
	newPath2 = wav(uuid, unique)
	os.remove(uuid)
	audio = wave.open(newPath2)
	samples = audio.readframes(BUFFER_SIZE)
	finished = False
	houndClient.start(MyListener())
	while not finished:
		finished = houndClient.fill(samples)
		time.sleep(0.032)			## simulate real-time so we can see the partial transcripts
		samples = audio.readframes(BUFFER_SIZE)
		if len(samples) == 0:
			break
	houndClient.finish()
	os.remove(newPath2)
	return(result)

@webapp.route("/api/houndifyTest")
def houndifyTest():
	audio = wave.open("test.wav")
	samples = audio.readframes(BUFFER_SIZE)
	finished = False
	houndClient.start(MyListener())
	while not finished:
		finished = houndClient.fill(samples)
		time.sleep(0.032)			## simulate real-time so we can see the partial transcripts
		samples = audio.readframes(BUFFER_SIZE)
		if len(samples) == 0:
			break
	houndClient.finish()
	return(result)


#server initializiation
if (__name__ == "__main__"):
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
