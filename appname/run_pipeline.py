from appname.poc.etl_pipeline import ETLPipeline

from in_pip.tmg_etl_runner import ETLInterface, ETLRunner

import sys
import click

PYTHON_MIN_VERSION = (3, 6)
APP_NAME = 'poc'  # Created in the template


@click.command()
@click.option('-c', '--config', required=True, type=str, help='Location of Configuration.\ngs://[bucket]/[config]\n/full/local/path)')
@click.option('-sd', '--start_date', required=False, type=click.DateTime(formats=['%Y%m%d']))
@click.option('-ed', '--end_date', required=False, type=click.DateTime(formats=['%Y%m%d']))
@click.option('-b', '--backfill', required=False, is_flag=True)
def instantiate_etl_runner(config, start_date, end_date, backfill):

    runner = ETLRunner(APP_NAME, config, ETLPipeline)  #TODO: Investigate passing all other click commands into this function?
    runner.run(start_date, end_date, backfill)


if __name__ == "__main__":
    assert tuple(sys.version_info) >= PYTHON_MIN_VERSION, "Please update to Python {}.{}".format(
        PYTHON_MIN_VERSION[0], PYTHON_MIN_VERSION[0])

    instantiate_etl_runner()
