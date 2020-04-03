import os
import logging
import logging.config
import yaml


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
LOGGING_FILENAME_PATH = os.path.join(MODULE_PATH, 'conf', 'logging.yml')


default_logging_dict = \
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "{app_name} %(levelname)9s %(asctime)3s Module: %(module)s - Line: %(lineno)s %(message)s"
            }
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout"
            },
            "errors": {
                "level": "ERROR",
                "formatter": "default",
                "class": "logging.StreamHandler"
            }
        },
        "loggers": {
            "default": {
                "handlers": [
                    "default",
                    "errors"
                ],
                "level": "INFO",
                "propagate": "no"
            }
        }
    }


class TMGLogging:

    def __init__(self, config, app_name):
        self.config = config
        self.app_name = app_name
        self._logger = self._get_logger()

    @property
    def logger(self):
        return self._logger

    def _get_logger(self):
        if self.config.get('logger'):
            logger = self._load_custom_logger()
        else:
            logger = self._load_default_logger()
        return logger

    def _load_default_logger(self, logging_config_file=LOGGING_FILENAME_PATH):

        logging.config.dictConfig(default_logging_dict)
        logger = logging.getLogger('default')
        return logger

    def _load_custom_logger(self):
        """
        :param logging_config: Dict of form
            {'use': 'name of logger to use from config', 'config': {dictConfig} }
            https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
        :return:
        """
        logging_config = self.config['logger']
        try:
            logger_to_use = logging_config['use']
            for formatter_name, format_dict in logging_config['config']['formatters'].items():
                logging_config['config']['formatters'][formatter_name]['format'] = format_dict['format'].format(app_name=self.app_name) #TODO: CLeanup
            logging.config.dictConfig(logging_config['config'])
            logger = logging.getLogger(logger_to_use)
            return logger
        except Exception:
            raise Exception('Custom Logging should be of form blah blah blah') # TODO: Clean up this exception catching

