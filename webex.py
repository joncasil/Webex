import json
import requests
from pprint import pprint
r = requests.get('https://webexapis.com/v1/people/me',headers={'Authorization': 'Bearer YzhiYTBlYTctMTVmNS00YTBjLWJjY2EtMDFiNWY4MzVkMmNiMWZjMjNiNWQtNWJk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f', 'accept': 'application/json'})

json_text= json.loads(r.text)

pprint(json_text) 

print(API2)

"""DO NOT USE THE SAME TOKEN"""
