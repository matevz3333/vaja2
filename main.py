import requests
import pprint
# pip install requests

baseUrl = "https://api.nationalize.io/?name=johnson"

"""for i in range(10):
    klic = requests.get(baseUrl)
    #print(klic)

    js = klic.json()
    #print(type(js), js)
    vic = js.get("value")
    print(vic)
    #pprint.pprint(js)"""


ime = input ("Vnesi ime: ")
klic = requests.get(baseUrl + ime)
print(klic.url) #pove kaksen klic je nastal
js = klic.json()

print(f"{js.get("count")=}")
print(f"{js.get("name")=}")

drzave = js.get("country")
for d in drzave:
    print(d.get("country_id"))
    print(d.get("probability"))