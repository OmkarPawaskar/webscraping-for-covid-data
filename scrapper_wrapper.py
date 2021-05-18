"""
Wrapper method to scrap data from url
"""

import config
from datascrapper import DataScrapper

COLUMN_LIST = ['TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases', 'Serious,Critical']
DROP_COLUMNS_LIST = ['#', 'NewRecovered', 'Tot\xa0Cases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/\n1M pop', 'Population', 'Continent', '1 Caseevery X ppl', '1 Deathevery X ppl', '1 Testevery X ppl', 'Serious,Critical']

def get_country_data():
    """ Gets Country dataframe from DataScrapper """
    data_scrapper = DataScrapper(config.URL_PATH, config.TABLE_ID, COLUMN_LIST, DROP_COLUMNS_LIST)
    country_dataframe = data_scrapper.run_process()
    return country_dataframe

