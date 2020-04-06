from in_pip.etl import TMGETLPipeline


class ETLPipeline(TMGETLPipeline):

    def run(self, start_date, end_date, backfill):

        self.logger.info('HELLO')
        self.logger.info('Start Date: %s' % start_date)
        self.logger.error('End Date: %s' % end_date)

        if backfill:
            self.logger.info('HERE')

    def graceful_shutdown(self):
        self.logger.info('GOODBYE')
