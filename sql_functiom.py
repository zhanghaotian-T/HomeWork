import sqlite3


class SqliteFunction(object):
    def __init__(self):
        self.con = sqlite3.connect('foods.db')

    def databasse_qurey(self):
        pass

    def database_write(self):
        pass
