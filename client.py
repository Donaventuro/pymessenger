import requests
from pprint import pprint

response = requests.get('http://localhost:9001')
pprint(response())
