import requests 

import random


ACCESS_KEY = 'XXXXXX'
Items = ['Water', 'water in cup', 'sea']
q = Items + ['Nature']

query = random.choice(q)
url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}'
response = requests.get(url)

data = response.json()["results"]





