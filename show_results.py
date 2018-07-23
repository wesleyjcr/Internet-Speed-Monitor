#!/usr/bin/python3

import os
import platform
from con_database import *
from prettytable import *
from speed_net import *

class Show_results:
    def __init__(self):
        self.connect_db = Connect_database()
        self.operational_system = platform.system()

    def main(self):
        if self.operational_system =='Windows':
            os.system('cls')    
        else:
            os.system('clear')
        chose_option = int(input('''
        VELOCIMETRO

                Autor : Wesley Ribeiro
                e-mail: wesleyjcr@gmail.com


1. Relatório do dia
2. Relatório do Ping
3. Relatório de Download
4. Relatório de Upload
5. Efetuar nova medição
6. Encerrar aplicação

Escolha uma opção:'''))

        if   chose_option == 1:
            self.data_day_report()
        elif chose_option == 2:
            self.data_ping_report()
        elif chose_option == 3:
            self.data_download_report()
        elif chose_option == 4:
            self.data_upload_report()
        elif chose_option == 5:
            self.test_speed()
        elif chose_option ==6:
            exit()
        else:
            input('Opção inválida!')


    def data_day_report(self):
        print('Medições do dia')
        self.row = PrettyTable()
        self.row.field_names = ['ID', 'PING', 'DOWNLOAD','UPLOAD','DATA','SERVIDOR']
        self.connect_db.connect()
        self.all_data = self.connect_db.get_day_mensurements()
        self.connect_db.disconnect()
        for self.linha in self.all_data:
            self.row.add_row(self.linha)
        print(self.row.get_string())
        input('Pressione enter para continuar...')

    def data_ping_report(self):
        print('Dados do Ping')
        self.row = PrettyTable()
        self.row.field_names = ['MAX', 'MIN', 'MED', 'DATE' ]
        self.connect_db.connect()
        self.data_ping = self.connect_db.get_data_ping()
        self.connect_db.disconnect()
        for self.linha in self.data_ping:
            self.row.add_row(self.linha)
        print(self.row.get_string())
        input('Pressione enter para continuar...')

    def data_download_report(self):
        print('Dados do Download')
        self.row = PrettyTable()
        self.row.field_names = ['MAX', 'MIN', 'MED', 'DATE' ]
        self.connect_db.connect()
        self.data_download = self.connect_db.get_data_download()
        self.connect_db.disconnect()
        for self.linha in self.data_download:
            self.row.add_row(self.linha)
        print(self.row.get_string())
        input('Pressione enter para continuar...')

    def data_upload_report(self):
        print('Dados do Upload')
        self.row = PrettyTable()
        self.row.field_names = ['MAX', 'MIN', 'MED', 'DATE' ]
        self.connect_db.connect()
        self.data_upload = self.connect_db.get_data_upload()
        self.connect_db.disconnect()
        for self.linha in self.data_upload:
            self.row.add_row(self.linha)
        print(self.row.get_string())
        input('Pressione enter para continuar...')

    def test_speed(self):
        print('O teste pode demorar alguns segundos, dependendo de sua conexão... AGUARDE UM POUCO')
        speed_net = Speed_net()
        speed_net.get_speed()
        speed_net.set_speed()
        connect_db = Connect_database()
        connect_db.connect()
        connect_db.do_insert(speed_net.data_persistence())
        connect_db.disconnect()

if __name__ == '__main__':
    show_results = Show_results()
    while True:
        show_results.main()




