import pandas as pd
import os
import datetime as dt
import settings

# There are three types called 'card-title', 'card-region-name', 'card-counts'

class Process:
    def __init__(self, object=None):
        self._data_object = object
        self._date = dt.datetime.now()   # to add a date data when making a dataframe
        self._path = os.path.join(settings.PROJ_ROOT, "data")

    def extract_item_name(self):
        raw_item_data = self._data_object.find_all('h2', class_="card-title")   # extract item data from crawled data
        self._item_column = []
        for item in raw_item_data:
            self._item_column.append(item.text)
        return self._item_column

    def extract_region_name(self):
        raw_region_data = self._data_object.find_all('div', class_="card-region-name")   # extract region data from crawled data
        region_list = []
        self._region_column = []
        for i, region in enumerate(raw_region_data):
            region_list.append(region.text.split('\n'))
            self._region_column.append(region_list[i][1])
        return self._region_column

    def extract_like_and_chat(self):
        raw_card_counts = self._data_object.find_all('div', class_="card-counts")   # extract chat and like data from crawled data
        split_list = []
        self._like_column = []
        self._chat_column = []
        for i, count in enumerate(raw_card_counts):
            split_list.append(count.text.split("\n"))
            self._like_column.append(split_list[i][2].replace(" ","")[-1])
            self._chat_column.append(split_list[i][6].replace(" ","")[-1])
        return self._like_column, self._chat_column

    # make a dataframe
    def make_dataframe(self):
        # save date before making dataframe
        date_data = str(self._date.strptime(self._date.strftime("%Y %m %d %X"), '%Y %m %d %X'))
        print(date_data)
        raw_data = {
            'local_name' : self._region_column,
            'item' : self._item_column,
            'like' : self._like_column,
            'chat' : self._chat_column
        }
        raw_data_df = pd.DataFrame(raw_data, columns=['local_name', 'item', 'like', 'chat'])
        
        # add a date data
        raw_data_df['date'] = date_data
        
        return raw_data_df


    def get_project_path(self):
        return self._path

    def __str__(self):
        result = str()
        return result