import traceback
from logger import logger
from scrapper_wrapper import get_country_data

if __name__  == '__main__':
    try:
        result = get_country_data()
        print(result)
        logger.info("Data loaded successfully!")
    except Exception as ex:
        error_template = "Error ocurred while running the process : An exception of type {0} occurred. Arguments:\n{1!r}"
        ERROR_MSG = error_template.format(type(ex).__name__, ex.args)
        logger.error(ERROR_MSG)
        error_trace = traceback.format_exc()
        logger.error(error_trace)