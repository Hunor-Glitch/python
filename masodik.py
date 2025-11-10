import requests

keres = input("Keres: ")
valasz = requests.get (keres)
print(valasz.status_code)
print(valasz.headers)
#print(valasz.text)
