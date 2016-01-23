import os
import sys
import logging
import json
from flask import Flask, Response, render_template, request, redirect, url_for, send_from_directory, g, session
from multiprocessing.pool import ThreadPool
from controller.query import *

webapp = Flask(__name__)
@webapp.route("/")
def root():
	return render_template('index.html')

# API Routes
# General format is "/api/<endpoint here>"
@webapp.route("/api/structure")
def query():
	return 0
@webapp.route("/api/review")
def review():
	return 0


#server initializiation
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
