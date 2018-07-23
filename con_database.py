#!/usr/bin/python3

import sqlite3, os

class Connect_database:
    def __init__(self):
        self.path_project = os.path.dirname(os.path.abspath(__file__)) 
        self.database_name = self.path_project+'/net_data.db'
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def do_insert(self, data_test):
        self.cursor.executemany("INSERT INTO DATA_NET (PING, DOWNLOAD, UPLOAD, DATE_TEST, SERVER, SHARE) VALUES (?,?,?,?,?,?)",data_test)
        self.conn.commit()
    
    def get_day_mensurements(self):
        self.cursor.execute('''SELECT ID, PING, printf('%.2f',DOWNLOAD/1000000), printf('%.2f',UPLOAD/1000000), STRFTIME('%d/%m/%Y', DATE_TEST) AS DATE_TEST, SERVER
                                FROM DATA_NET 
                                ORDER BY ID DESC LIMIT 25''')
        return self.cursor.fetchall()
    
    def get_data_ping(self):
        self.cursor.execute('''SELECT 
            PRINTF('%.2f',MAX(PING)) as MAX
            ,PRINTF('%.2f',MIN(PING)) as MIN
            ,PRINTF('%.2f',AVG(PING)) AS MED
            ,strftime('%d/%m/%Y',DATE_TEST) as DATE
        FROM DATA_NET
        GROUP BY strftime('%d/%m/%Y',DATE_TEST)
        ''')
        return self.cursor.fetchall()

    def get_data_download(self):
        self.cursor.execute('''SELECT 
            PRINTF('%.2f',MAX(DOWNLOAD)/1000000) as MAX
            ,PRINTF('%.2f',MIN(DOWNLOAD)/1000000) as MIN
            ,PRINTF('%.2f',AVG(DOWNLOAD)/1000000) AS MED
            ,strftime('%d/%m/%Y',DATE_TEST) as DATE
        FROM DATA_NET
        GROUP BY strftime('%d/%m/%Y',DATE_TEST)
        ''')
        return self.cursor.fetchall()

    def get_data_upload(self):
        self.cursor.execute('''SELECT 
            PRINTF('%.2f',MAX(UPLOAD)/1000000) as MAX
            ,PRINTF('%.2f',MIN(UPLOAD)/1000000) as MIN
            ,PRINTF('%.2f',AVG(UPLOAD)/1000000) AS MED
            ,strftime('%d/%m/%Y',DATE_TEST) as DATE
        FROM DATA_NET
        GROUP BY strftime('%d/%m/%Y',DATE_TEST)
        ''')
        return self.cursor.fetchall()