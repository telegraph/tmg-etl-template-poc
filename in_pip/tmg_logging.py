import os
import logging
import logging.config
import yaml


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
LOGGING_FILENAME_PATH = os.path.join(MODULE_PATH, 'conf', 'logging.yml')


class TMGLogging:

    def __init__(self, config, app_name):
        self.config = config
        self.app_name = app_name

    def get_logger(self):
        if self.config.get('logger'):
            logger = self._load_custom_logger()
        else:
            logger = self._load_default_logger()
        return logger

    def _load_default_logger(self, logging_config_file=LOGGING_FILENAME_PATH):
        with open(logging_config_file, 'rt') as logging_file:
            logging_dict_config = yaml.load(logging_file, Loader=yaml.SafeLoader)
            logging_dict_config['formatters']['default']['format'] = logging_dict_config['formatters']['default']['format'].format(app_name=self.app_name)
            logging.config.dictConfig(logging_dict_config)

            logger = logging.getLogger('default')

            return logger

    def _load_custom_logger(self):
        """
        :param logging_config: Dict of form
            {'name': 'name of logger to use from config', 'config': {dictConfig} }
            https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
        :return:
        """
        logging_config = self.config['logger']
        try:
            logger_to_use = logging_config['name']
            for formatter_name, format in  logging_config['config']['formatters']:
                logging_config['config']['formatters'][formatter_name] = logging_config['config']['formatters'][formatter_name].format(app_name=self.app_name) #TODO: CLeanup
            logger = logging.getLogger(logger_to_use)
            logging.config.dictConfig(logging_config['config'])
            return logger
        except Exception:
            raise Exception('Custom Logging should be of form blah blah blah') # TODO: Clean up this exception catching