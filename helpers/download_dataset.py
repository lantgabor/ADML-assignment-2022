import os
import wget
import tarfile


def extract_data(path, filename):
    if filename.endswith(".bz2\n"):
        print("Extracting file: ", filename, "bz2")
        with tarfile.open(filename, "r:bz2") as tar:
            tar.extractall(path=os.path.join(path, "out"))
            tar.close()
    elif filename.endswith(".gz\n"):
        print("Extracting file: ", filename, "gz")
        with tarfile.open(filename, "r:gz") as tar:
            tar.extractall(path=os.path.join(path, "out"))
            tar.close()
    elif filename.endswith(".tar\n"):
        print("Extracting file: ", filename, "tar")
        with tarfile.open(filename, "r:") as tar:
            tar.extractall(path=os.path.join(path, "out"))
            tar.close()
    else:
        print(filename)


def download_data(urls, path):

    # create data directory
    final_directory = os.path.join(os.getcwd(), path)
    os.makedirs(final_directory, exist_ok=True)

    # download datasets
    for url in open(urls):
        name = os.path.basename(url)
        filename = os.path.join(path, name)

        if not os.path.isfile(filename):
            # print("Downloading: {}".format(filename))
            wget.download(url, out=filename)

            extract_data(path, filename)


download_data("./helpers/shakefive2.txt", "./data/shakefive2")
download_data("./helpers/tv_human.txt", "./data/tv_human")
