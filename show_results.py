#!/usr/bin/python3

import os
from con_database import *
from prettytable import *

class Show_results:
    def __init__(self):
        self.connect_db = Connect_database()
        

    def main(self):
        os.system('clear')
        chose_option = int(input('''
        VELOCIMETRO

                Autor : Wesley Ribeiro
                e-mail: wesleyjcr@gmail.com


1. Relatório do dia
2. Relatório do Ping
3. Relatório de Download
4. Relatório de Upload
5. Encerrar aplicação

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
            exit()
        else:
            print('Opção inválida!')


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

if __name__ == '__main__':
    show_results = Show_results()
    while True:
        show_results.main()




