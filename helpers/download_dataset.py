import os
import requests

def download_data(urls, out_dir):
    for url in open(urls):
        name = os.path.basename(url)
        filename = os.path.join(out_dir, name)

        if not os.path.isfile(filename):
            r = requests.get(url)
            open(filename, 'wb').write(r.content)


download_data('./helpers/shakefive2.txt', './data/shakefive2')
download_data('./helpers/tv_human.txt', './data/tv_human')