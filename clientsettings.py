import configparser
import os

class ClientSettings:

    config = configparser.ConfigParser()

    def __init__(self, filename):
        self.filename = filename
        self.server_ip = None
        self.server_user = None
        self.remote_folder = None


    def load(self):
        self.config.read(self.filename)
        self.server_ip = self.config['GENERAL']['server_ip']
        self.server_user = self.config['GENERAL']['server_user']
        self.remote_folder = self.config['GENERAL']['remote_folder']


    def write(self):
        self.config.add_section('GENERAL')
        self.config.set('GENERAL', 'server_ip', self.server_ip)
        self.config.set('GENERAL', 'server_user', self.server_user)
        self.config.set('GENERAL', 'remote_folder', self.remote_folder)


        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)
