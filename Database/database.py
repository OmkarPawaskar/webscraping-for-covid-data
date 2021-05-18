"""
This module contains functions to  connect to sql server database and returns the connection
"""

from logger import logger
import json
import psycopg2

class DatabaseConnection:
    """init function
    Args:
        config_file (str): the filepath where database configuration file is. This includes the file name
    """