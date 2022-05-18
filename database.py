import sqlite3 as sql
import datetime

class Database:
    __CREATE_TABLE_DATA__ = r'CREATE TABLE data(timestamp text, key text, value text);'
    __INSERT_VALUES_SQL__ = r"INSERT INTO data (timestamp,key,value) VALUES ('{timestamp}','{key}','{value}')"
    __MIGRATION__ = [__CREATE_TABLE_DATA__]

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.get_connection()
        try:
            self.__init_db__()
        except:
            print('DB JA INICIADO')

    def get_connection(self):
        return sql.connect(self.db_name)

    def get_cursor(self):
        return self.connection.cursor()

    def __init_db__(self):
        for script in self.__MIGRATION__:
            self.get_cursor().execute(script)
            self.connection.commit()

    def insert_values(self, key, value):
        date = datetime.datetime.now()
        statement = self.__INSERT_VALUES_SQL__.format(timestamp=str(date), key=key, value=value)
        print(statement)
        self.get_cursor().execute(statement)
        self.connection.commit()

    def copy_clean(self, data):
        statement = self.__INSERT_VALUES_SQL__.format(timestamp=str(data[0]), key=data[1], value=data[2])
        print(statement)
        self.get_cursor().execute(statement)
        self.connection.commit()

