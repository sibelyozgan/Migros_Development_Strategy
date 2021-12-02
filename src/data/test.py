#%load_ext lab_black


import json
import requests
from pandas import json_normalize

url = "https://ckan.opendata.swiss/api/3/action/package_show?id=durchschnittlicher-mietpreis-in-franken-nach-altersgruppe-der-haushaltsmitglieder-und-grossregi2"

test_json = requests.get(url).json()
print(test_json["result"])



