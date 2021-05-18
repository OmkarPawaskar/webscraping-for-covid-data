from urllib.request import urlopen, Request
import pandas as pd
from bs4 import BeautifulSoup as soup
from datetime import datetime, timedelta
import config
from logger import logger

class DataScrapper():

    def __init__(self, url, id, column_list, drop_list):
        self.url = url
        self.id = id
        self.column_list = column_list
        self.drop_list = drop_list
        self.dataset = None
        

    def scrape_data(self):
        """
        Returns a table of content scrapped from web.
        """
        req = Request(self.url, headers={'User-Agent' : 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup_web = soup(webpage, "html.parser")
        table = soup_web.find("table", {"id" : self.id})
        return table
    
    def get_data_content(self, table):
        """
        Gets required header and row details
        """
        rows = table.find_all("tr")
        headers = table.find_all("th")
        headers = [header.get_text().strip('\n') for header in headers]
        data_content = []
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 1:
                country_info = [cell.text.strip() for cell in cells]
                data_content.append(country_info)
        return data_content,headers

    def convert_to_dataframes(self, data_content, headers):
        """
        Converts data_content to pandas df.
        """
        self.dataset = pd.DataFrame(data_content)
        self.dataset.columns = headers

    def apply_filters(self):
        """
        Applies Additional filters on dataframe columns 
        """
        for column in self.column_list:
            self.dataset[column] = self.dataset[column].str.replace(',','')
            self.dataset[column] = self.dataset[column].str.replace('+','')
            self.dataset[column] = self.dataset[column].str.replace('-','')
            if column == "Serious,Critical":
                self.dataset['Serious/Critical'] = self.dataset["Serious,Critical"]
        return

    def dataset_modifiers(self):
        """
        Drops given list of columns and adds timestamp
        """
        self.dataset.drop(self.drop_list, axis=1, inplace=True)
        now = datetime.now()
        yesterday = now - timedelta(days = 1)
        yesterday = yesterday.date()
        self.dataset.insert(0, 'TimeStamp', yesterday)
        self.dataset.replace("N/A","", inplace=True)
        return 
    
    def run_process(self):
        """
        Wrapper method to run whole process
        """
        try:
            table = self.scrape_data()
            data_content,headers = self.get_data_content(table)
            self.convert_to_dataframes(data_content,headers)
            self.apply_filters()
            self.dataset_modifiers()
            return self.dataset
        except Exception as ex:
            logger.error("Exception occured while fetching data from URL %s",ex)
            

        