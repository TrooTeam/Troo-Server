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
import crud
import Analize
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool

houndClient = houndify.StreamingHoundClient("F98d-lDRNRHV91T7LFIiKqHAZauzZbsvytojjNyFqr8sdZTl_9UmMjW4joxKqTJO7w688WUi7Cl1tRCjst3WRw==",
											"2z8RgKlFDs2paNd-opTnmQ==")
# spoof location
houndClient.setLocation(37.388309, -121.973968)
BUFFER_SIZE = 512



class reviewListener(houndify.HoundListener):

	def onPartialTranscript(self, transcript):
		print "Partial transcript: " + transcript
	def onFinalResponse(self, response):
		print "Final response: " + str(response)

		#Put the handling here for reviewing?
	def onTranslatedResponse(self, response):
		print "Translated response: " + response
	def onError(self, err):
		print "ERROR"




# WAV Encoding function
def wav(filePath, name):
	os.system("track2track -t wav *m4a")



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
def update(id, params):
	return put(id, params);

@webapp.route("/api/oldSpeech2Text")
def oldSpeech2text():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks/vYGZor1rHD', '', {
	connection.request('GET', '/1/classes/Feedbacks/P784yfn1qi', '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	uuid = unique + ".m4a"
	urllib.urlretrieve (url, uuid)
	newPath2 = wav(uuid, unique)
	os.remove(uuid)
	audio = wave.open(newPath2)
	# os.remove(uuid)
	samples = audio.readframes(BUFFER_SIZE)
	finished = False
	houndClient.start(reviewListener())
	while not finished:
		finished = houndClient.fill(samples)
		time.sleep(0.032)			## simulate real-time so we can see the partial transcripts
		samples = audio.readframes(BUFFER_SIZE)
		if len(samples) == 0:
			break
	houndClient.finish()
	os.remove(newPath2)
	return("Houndify Finished.")

@webapp.route("/api/houndifyTest")
def houndifyTest():
	audio = wave.open("test.wav")
	samples = audio.readframes(BUFFER_SIZE)
	finished = False
	houndClient.start(reviewListener())
	while not finished:
		finished = houndClient.fill(samples)
		samples = audio.readframes(BUFFER_SIZE)
		if len(samples) == 0:
			break
	houndClient.finish()
	return(result)


#server initializiation
if (__name__ == "__main__"):
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
