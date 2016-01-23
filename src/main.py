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
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool

houndClient = houndify.StreamingHoundClient("F98d-lDRNRHV91T7LFIiKqHAZauzZbsvytojjNyFqr8sdZTl_9UmMjW4joxKqTJO7w688WUi7Cl1tRCjst3WRw==",
											"2z8RgKlFDs2paNd-opTnmQ==")


def wav(filePath, name):
	newName = name + ".wav"
	at = audiotranscode.AudioTranscode()
	at.transcode(filePath, newName)
	return 0

class MyListener(houndify.HoundListener):
	def onPartialTranscript(self, transcript):
		print "Partial transcript: " + transcript
	def onFinalResponse(self, response):
		print "Final response: " + str(response)
	def onTranslatedResponse(self, response):
		print "Translated response: " + response
	def onError(self, err):
		print "ERROR"



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
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Feedbacks', json.dumps(data), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()

@webapp.route("/api/read")
def read():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks', '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()

@webapp.route("/api/update")
def update():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('PUT', '/1/classes/Feedbacks', json.dumps({
       "score": 1337,
       "playerName": "Sean Plott",
       "cheatMode": False
     }), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()

@webapp.route("/api/speech2text")
def speech2text():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks/Vhb84o3k9P', '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	# testObj = connection.getresponse().read()
	result = json.loads(connection.getresponse().read().decode("utf-8"))
	url = result["audioFile"]["url"]
	unique = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
	uuid = unique + ".m4a"
	urllib.urlretrieve (url, uuid)
	wav(uuid, unique)

	return("success")


#server initializiation
if (__name__ == "__main__"):
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
