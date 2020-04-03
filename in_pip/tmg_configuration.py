import os
import yaml

from google.cloud import storage


class ConfigurationLoader:

    def __init__(self, config_location):
        self.config_location = config_location
        self._config = self._load_config()

    @property
    def config(self):
        return self._config

    def _load_config(self):

        if self.config_location[:2] == 'gs':
            return self._load_config_from_gs()
        elif os.path.isfile(self.config_location):
            return self._load_config_from_local()
        else:
            return self._load_config_from_env()

    def _load_config_from_gs(self):
        try:
            bucket, file = self.config_location.replace('gs://', '').split('/')
        except ValueError:
            raise RuntimeError('Config Location must be of form "bucket/file"')
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket)
        file = bucket.blob(file)
        file_content = file.download_as_string()

        return yaml.load(file_content, Loader=yaml.SafeLoader)

    def _load_config_from_local(self):
        with open(self.config_location, 'rt') as file:
            file_content = file.read()

        return yaml.load(file_content, Loader=yaml.SafeLoader)

    def _load_config_from_env(self):
        config = os.getenv(self.config_location)
        if not config:
            raise Exception('Config not loaded, please provide valid filepath, GS URI, or environment variable')

        return yaml.load(config)
