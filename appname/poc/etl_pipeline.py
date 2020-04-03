from in_pip.tmg_etl_runner import ETLInterface


class ETLPipeline(ETLInterface):

    def run_pipeline(self, start_date, end_date, backfill):

        self.logger.info('HELLO')
        self.logger.info('Start Date: %s' % start_date)
        self.logger.error('End Date: %s' % end_date)

        if backfill:
            self.logger.info('HERE')

    def graceful_shutdown(self):
        self.logger.info('GOODBYE')
