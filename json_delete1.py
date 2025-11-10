import requests

res = input("Adj meg egy torlendo autot! ")

try:
	valasz  = requests.delete("http://127.0.0.1:3000/autok/" + res)
except:
        print("Hiba tortent!")
        exit()
print(valasz.status_code)
#print(valasz.headers)
print(valasz.text)
