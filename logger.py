"""
This module contains logging configurations
"""

from datetime import datetime
import logging
import config 

LOG_PATH = config.LOG_PATH
yearMonth = datetime.today().strftime('%Y%m%d-%H%M%S')
logFileName = f"CovidDataLoad-{yearMonth}.log"
logging.basicConfig(level=logging.INFO,
                    filename = f'logs/{logFileName}',
                    format = "%(asctime)s %(levelname)-8s %(message)s",
                    datefmt = "%Y%m%d %H:%M:%S",
                    filemode = 'a')

logger = logging.getLogger("Covid-19 Data Loader")