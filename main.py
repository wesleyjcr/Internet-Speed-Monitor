#!/usr/bin/python3.5

from con_database import *
from speed_net import *

if __name__ == '__main__':
    speed_net = Speed_net()
    speed_net.get_speed()
    speed_net.set_speed()
    connect_db = Connect_database()
    connect_db.connect()
    connect_db.do_insert(speed_net.data_persistence())
    connect_db.disconnect()