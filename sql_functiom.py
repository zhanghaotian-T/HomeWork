import sqlite3
import pandas as pd
from sqlalchemy import create_engine


class SqliteFunction(object):
    def __init__(self):
        self.con = sqlite3.connect('foods.db')
        self.engine = create_engine('sqlite:///foods.db')

    def databasse_qurey(self,dataframe):
        pass

    def database_write(self, dataframe):
        dataframe['']
        dataframe.to_sql('foods', con=self.engine, if_exists='append')
