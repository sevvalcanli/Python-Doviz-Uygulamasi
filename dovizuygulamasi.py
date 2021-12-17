import requests
import sys
url = "https://api.exchangeratesapi.io/latest?base="


birinci_doviz = input("Birinci döviz: ")
ikinci_doviz = input("İkinci Döviz: ")
miktar = float(input("Miktar: "))
response = requests.get(url + birinci_doviz)

json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_doviz]*miktar)
except KeyError:
    sys.stderr.write("Para birimlerini doğru girin.")
    sys.stderr.flush()