import os
from numpy import iterable
import wget
import tarfile
from tqdm import tqdm


def extract_data(path, filename):

    if filename.endswith(".bz2"):
        # print("Extracting file: ", filename, "bz2")
        with tarfile.open(filename, "r:bz2") as tar:
            for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
                tar.extract(member=member, path=os.path.join(path, "out"))
            tar.close()
    elif filename.endswith(".gz"):
        # print("Extracting file: ", filename, "gz")
        with tarfile.open(filename, "r:gz") as tar:
            for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
                tar.extract(member=member, path=os.path.join(path, "out"))
            tar.close()
    elif filename.endswith(".tar"):
        # print("Extracting file: ", filename, "tar")
        with tarfile.open(filename, "r:") as tar:
            for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
                tar.extract(member=member, path=os.path.join(path, "out"))
            tar.close()
    else:
        print(filename)


def download_data(urls, path):

    # create data directory
    final_directory = os.path.join(os.getcwd(), path)
    os.makedirs(final_directory, exist_ok=True)

    # download datasets
    for url in open(urls):
        url = url.strip()
        name = os.path.basename(url)
        filename = os.path.join(path, name)

        if not os.path.isfile(filename):
            print("Downloading: {}\n".format(filename))
            wget.download(url, out=filename)

        extract_data(path, filename)


# download_data("./helpers/shakefive2.txt", "./data/shakefive2")
# download_data("./helpers/tv_human.txt", "./data/tv_human")
download_data("./helpers/anet.txt", "./data/anet")
