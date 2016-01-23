import os
import sys
import logging
import json
import http.client
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool
#
# connection = http.client.HTTPSConnection('api.parse.com', 443)
# connection.connect()
# connection.request('GET', '/1/classes/Feedbacks', '', {
#        "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
#        "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
#      })
# result = json.loads(connection.getresponse().read().decode("utf-8"))
# print(result)


webapp = Flask(__name__)
@webapp.route("/")
def root():
	return render_template('index.html')

# API Routes
# General format is "/api/<endpoint here>"
@webapp.route("/api/create")
def create():
	return 0

@webapp.route("/api/read")
def read():
	return 0

@webapp.route("/api/update")
def update():
	return 0

@webapp.route("/api/delete")
def update():
	return 0


#server initializiation
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
