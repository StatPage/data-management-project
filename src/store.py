import sqlite3
from elasticsearch import Elasticsearch
import pandas as pd

class SQL:
    def __init__(self, database=None, root=None):
        self._db = database
        self._root = root

    def get_cur_with_db(self, database=None):
        if database != None:
            self._db = database
        if self._db == None:
            print("Please select a database")
        self._connection = sqlite3.connect(database)
        self._cursor = self._connection.cursor()

        return self._cursor

    def load_csv_and_create_table(self, table_name, data):
        self._raw_data_csv = pd.read_csv(data)
        self._raw_data_csv.to_sql(table_name, self._connection, if_exists='replace', index=False)

    def close(self):
        self._connection.close()

    def __str__(self):
        result = str()
        return result



class Elastic:
    def __init__(self, host=None, data=None):
        self._host = host
        self._data = data
        self._es = Elasticsearch(self._host)

    def get_es(self):
        return self._es

    def load_and_convert_json(self, data):
        raw_data_json = pd.read_json(data)
        raw_data_json_index = raw_data_json.to_dict('index')
        return raw_data_json_index

        
    def __str__(self):
        result = str()
        return result