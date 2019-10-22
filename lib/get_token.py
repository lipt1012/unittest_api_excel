import requests
import json

def getToken():
	res = requests.post(
		url = "***",
		json = {"username": "***","password": "***"},
		headers = {"Content-Type":"application/json"},timeout = 5)
	return res.json()['result']['token']





