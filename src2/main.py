import os
import sys
import logging
import json
import httplib
import urllib
import time
import crud
import speechRecognition
from time import sleep
from threading import Timer



def hello():
    empties = crud.get({"reviewText" : None})
    empties = empties["results"]
    counter = 0;
    for a in empties:
        counter = counter + 1
        x = a["objectId"]
        speechRecognition.formatEntry(x,counter)

while True:
    hello()
    sleep(45) # your long-running job goes here...
