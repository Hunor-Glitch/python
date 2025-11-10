import requests
import json

uj_auto = { 
        "id": 5,
      "marka": "Ford",
      "tipus": "Galaxy",
      "evjarat": 2020,
      "kilometer": 55000,
      "motor": {
        "tipus": "benzin",
        "hengeruri": 1500,
        "teljesitmeny": 180,
        "uzemanyag": "benzin"
      },
      "felszereltseg": {
        "klima": True,
        "navigacio": True,
        "b ^qr": False,
        "parkolovalto": True,
        "kamera": False
      },
      "szin": "k  k",
      "ajanlott_ar": 3200000,
      "allapot": "  j",
      "tulajdonosok_szama": 0,
      "regisztracio_datum": "2021-11-10",
      "megjegyzesek": "Friss m  szaki vizsga."
        } 
h_tartalom = {'Content-Type': 'application/json'}
try:
	valasz = requests.post("http://127.0.0.1:3000/autok", headers=h_tartalom, data=json.dumps(uj_auto))
except:
	print("Nem fut a szerver!")
	exit()
print(valasz.status_code)
#print(valasz.headers)
#print(valasz.text)
