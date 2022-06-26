import requests 

import random


ACCESS_KEY = 'aDQdki2pX9d3BggPnyDGYl3n2UdmK3D_vmVpUQwZ99A'
Items = ['Water', 'water in cup', 'sea']
q = Items + ['Nature']

query = random.choice(q)
url = f'https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}'
response = requests.get(url)

data = response.json()["results"]





