import os
import sys
import logging
import json
import http.client
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool


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
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Feedbacks', json.dumps(data), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()

@webapp.route("/api/read")
def read():
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks', '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return connection.getresponse().read()

@webapp.route("/api/update")
def update():
	connection = http.client.HTTPSConnection('api.parse.com', 443)
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



#server initializiation
if (__name__ == "__main__"):
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
