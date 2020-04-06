from appname.poc.etl_pipeline import ETLPipeline

import sys
import click

PYTHON_MIN_VERSION = (3, 6)
APP_NAME = 'poc'  # Created in the template


@click.command()
@click.option('-c', '--config', required=True, type=str,
              help='Location of Configuration.\ngs://[bucket]/[config]\n/full/local/path)')
@click.option('-sd', '--start_date', required=False, type=click.DateTime(formats=['%Y%m%d']))
@click.option('-ed', '--end_date', required=False, type=click.DateTime(formats=['%Y%m%d']))
@click.option('-b', '--backfill', required=False, is_flag=True)
def runner(config, start_date, end_date, backfill):

    etl = ETLPipeline(APP_NAME, config)
    etl.execute(start_date, end_date, backfill)


if __name__ == "__main__":
    assert tuple(sys.version_info) >= PYTHON_MIN_VERSION, "Please update to Python {}.{}".format(
        PYTHON_MIN_VERSION[0], PYTHON_MIN_VERSION[0])

    runner()
