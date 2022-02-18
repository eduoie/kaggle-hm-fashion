import logging
import kaggle
import utils
import os

from config_info import download_dir

logger = logging.getLogger("download-kaggle-data")


# This dataset is 100k files, so it is better to download it and unzip it even if it requires twice the space temporarily
# dataset is 28.7 GB
def download_data():
    api = kaggle.api
    # UNNEEDED api.set_config_value('path', os.path.join(os.getcwd(), download_dir))
    api.competition_download_files('h-and-m-personalized-fashion-recommendations',
                                   path=os.path.join(os.getcwd(), download_dir), force=False, quiet=False)


def main():
    download_data()


if __name__ == '__main__':
    FORMAT = "%(asctime)s %(filename)s(l:%(lineno)d, p:%(process)d) - %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    main()
