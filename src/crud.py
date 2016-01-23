import httplib
import json

def post(params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Feedbacks', json.dumps(params), {
	       "X-Parse-Application-Id": "cBl3nISVOAT6ryXczsTeQFAiEr0os9oYWXUJHpKb",
	       "X-Parse-REST-API-Key": "GokaVtTay8vWCQeydQZzC4neVhIDhz5OnsyuWd9G"
	})
	return connection.getresponse().read()

def put(selector, params):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('PUT', '/1/classes/Feedbacks/'+selector, json.dumps(params), {
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
