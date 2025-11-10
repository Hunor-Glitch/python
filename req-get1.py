import requests

v = input("Adj meg egy eroforrast ")
try:
	v  = requests.get("http://localhost:3000/autok" + v)
except:
	print("Hiba tortent!")
	exit()
print(s.status_code)
print(s.text)
