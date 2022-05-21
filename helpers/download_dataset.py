import os
import urllib.request

urls = [
    "http://www2.projects.science.uu.nl/shakefive/data/ShakeFive2.background.tar.bz2",
    "http://www2.projects.science.uu.nl/shakefive/data/ShakeFive2.metadata.tar.bz2",
    "http://www2.projects.science.uu.nl/shakefive/data/ShakeFive2.videos.tar",
    "http://www2.projects.science.uu.nl/shakefive/data/ShakeFive2.code.tar.gz",
]

# For every line in the file
for url in urls:
    # Split on the rightmost / and take everything on the right side of tha
    name = url.rsplit("/", 1)[-1]

    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join(url, name)

    # Download the file if it does not exist
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)
