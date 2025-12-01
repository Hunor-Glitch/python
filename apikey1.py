import requests
import json

url="https://api.thecatapi.com/v1/breeds"

h={'x-api-key': 'DEMO_API_KEY'}
valasz  = requests.get(url, headers=h)
if valasz.status_code == 200:
	print(valasz.json())
else:
	print(valasz.status_code)
