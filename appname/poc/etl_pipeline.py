from in_pip.tmg_etl_runner import ETLInterface


class ETLPipeline(ETLInterface):

    def __init__(self, config, logger):
        self.config = config  # Loaded by default by ETLRunner
        self.logger = logger  # Loaded by default by ETLRunner

    def run_pipeline(self, **kwargs):
        start_date = kwargs['start_date']
        end_date = kwargs['end_date']

        self.logger.info('HELLO')
        self.logger.info('Start Date: %s' % start_date)
        self.logger.error('End Date: %s' % end_date)

    def graceful_shutdown(self):
        self.logger.info('GOODBYE')
