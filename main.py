#!/usr/bin/python3.5

import speedtest
import datetime
from con_database import *

class Speed_net:
    def __init__(self):
        self.spd_test = speedtest.Speedtest()
        self.ping = None
        self.download = None
        self.upload = None
        self.timestamp = None
        self.server = None
 
    def get_speed(self):
        self.spd_test.get_best_server()
        self.spd_test.download()
        self.spd_test.upload()
        self.tst_speed = self.spd_test.results.dict()

    def set_speed(self):
        self.ping = self.tst_speed['ping']
        self.download = self.tst_speed['download']
        self.upload =  self.tst_speed['upload']
        self.timestamp = datetime.datetime.now() 
        self.server = self.tst_speed['server']

    def data_persistence(self):
        data_test = [(
            self.ping,
            self.download,
            self.upload,
            self.timestamp,
            self.server['sponsor'])]
        return data_test

def main():
    speed_net = Speed_net()
    speed_net.get_speed()
    speed_net.set_speed()
    connect_db = Connect_database()
    connect_db.connect()
    connect_db.do_insert(speed_net.data_persistence())
    connect_db.disconnect()



if __name__ == '__main__':
    main()