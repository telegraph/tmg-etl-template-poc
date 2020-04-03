from in_pip.tmg_etl_runner import ETLInterface


class ETLPipeline(ETLInterface):

    def __init__(self, config, logger):
        self.config = config  # Loaded by default by ETLRunner
        self.logger = logger  # Loaded by default by ETLRunner

    def run_pipeline(self, start_date, end_date, backfill):

        self.logger.info('HELLO')
        self.logger.info('Start Date: %s' % start_date)
        self.logger.error('End Date: %s' % end_date)

        if backfill:
            self.logger.info('HERE')

    def graceful_shutdown(self):
        self.logger.info('GOODBYE')
