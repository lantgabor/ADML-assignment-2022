import os
import requests

for url in open('./helpers/urls.txt'):
    
    name = os.path.basename(url)
    filename = os.path.join('./data', name)

    if not os.path.isfile(filename):
        r = requests.get(url)
        open(filename, 'wb').write(r.content)