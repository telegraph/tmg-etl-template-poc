from in_pip.tmg_configuration import ConfigurationLoader
from in_pip.tmg_logging import TMGLogging

import abc
import os

GOOGLE_APP_CREDENTIALS_ENV_NAME = 'GOOGLE_APPLICATION_CREDENTIALS'
GOOGLE_CREDENTIALS_PATH = '/google-keys'


class ETLRunner:

    def __init__(self, app_name, config_location, etl_pipeline):

        self.config = ConfigurationLoader(config_location).config
        os.environ[GOOGLE_APP_CREDENTIALS_ENV_NAME] = self.config['service_account']
        self.logger = TMGLogging(self.config, app_name).logger
        self.pipeline = etl_pipeline(self.config, self.logger)

    def run(self, *args, **kwargs):
        try:
            self.pipeline.run_pipeline(*args, **kwargs)
        finally:
            self.pipeline.graceful_shutdown()


class ETLInterface(metaclass=abc.ABCMeta): #TODO: Find out what the different ABC types are

    @abc.abstractmethod
    def run_pipeline(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def graceful_shutdown(self, *args, **kwargs):
        pass
