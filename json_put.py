import requests
import json

# adat
uj_auto = {
        "id": 5,
      "marka": "Ford",
      "tipus": "Galaxy",
      "evjarat": 2019,
      "kilometer": 45000,
      "motor": {
        "tipus": "benzin",
        "hengeruri": 1498,
        "teljesitmeny": 170,
        "uzemanyag": "benzin"
      },
      "felszereltseg": {
        "klima": True,
        "navigacio": False,
        "b ^qr": False,
        "parkolovalto": True,
        "kamera": False
      },
      "szin": "k  k",
      "ajanlott_ar": 3000000,
      "allapot": "  j",
      "tulajdonosok_szama": 0,
      "regisztracio_datum": "2021-11-10",
      "megjegyzesek": "Friss m  szaki vizsga."
        }

# adat tipusa
h_tartalom = {'Content-Type': 'application/json'}

try:
	valasz = requests.put("http://127.0.0.1:3000/autok/5", headers=h_tartalom, data=json.dumps(uj_auto))
except:
	print("Nem fut a szerver!")
	exit()
print(valasz.status_code)
#print(valasz.headers)
#print(valasz.text)
