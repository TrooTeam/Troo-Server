import httplib
import urllib
import json

def post(params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Feedbacks', json.dumps(params), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	})
	return json.loads(connection.getresponse().read().decode("utf-8"))

def put(selector, params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('PUT', '/1/classes/Feedbacks/'+selector, json.dumps(params), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return json.loads(connection.getresponse().read().decode("utf-8"))


def get(params):
	params = urllib.urlencode({"where":json.dumps(params)})
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Feedbacks?%s' % params, '', {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	     })
	return json.loads(connection.getresponse().read().decode("utf-8"))
