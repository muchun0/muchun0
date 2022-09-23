from ast import main
import configparser
import os

def readConfig(section,options):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__),'config.ini'))
    return config[section][options]
if __name__ == '__main__':
    print(readConfig('ONLINE','url'))