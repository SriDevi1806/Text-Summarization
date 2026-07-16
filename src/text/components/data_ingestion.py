import os
import urllib.request as request
import zipfile
from pathlib import Path

from text.logging import logger
from text.utils.common import get_size
from text.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download the dataset if it doesn't already exist.
        """
        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} downloaded successfully!")
            logger.info(headers)

        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extract the zip file into the data ingestion directory.
        If the downloaded file is not a zip file, skip extraction.
        """

        if str(self.config.local_data_file).endswith(".zip"):

            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info("Zip file extracted successfully.")

        else:
            logger.info("Downloaded file is not a zip file. Skipping extraction.")