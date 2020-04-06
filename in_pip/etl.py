from in_pip.configuration import ConfigurationLoader
from in_pip.logging import TMGLogging

import abc
import os

GOOGLE_APP_CREDENTIALS_ENV_NAME = 'GOOGLE_APPLICATION_CREDENTIALS'
GOOGLE_CREDENTIALS_PATH = '/google-keys'


class TMGETLPipeline(metaclass=abc.ABCMeta): #TODO: Find out what the different ABC types are

    def __init__(self, app_name, config_path):
        self.app_name = app_name
        self.config = ConfigurationLoader(config_path).config
        self.logger = TMGLogging(self.config, app_name).logger

        if not os.environ.get(GOOGLE_APP_CREDENTIALS_ENV_NAME):
            os.environ[GOOGLE_APP_CREDENTIALS_ENV_NAME] = self.config['service_account']

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        pass

    def graceful_shutdown(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):

        try:
            self.run(*args, **kwargs)
        finally:
            self.graceful_shutdown()

