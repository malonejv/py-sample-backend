
from configparser import ConfigParser
from json.decoder import JSONDecodeError
import os
import sys
import json
import yaml


class ConfigKeys:
    ENABLE_THEME = "EnableTheme"
    LOGIN_USER = "User"
    LOGIN_PASSWORD = "Password"

class ConfigHelper:
    __CONFIG_FILE = 'config.json'

    __config = dict()

    def __init__(self, configFile = "config.ini"):
        self.__CONFIG_FILE = configFile
        self.__CONFIG_PATH = self.__getConfigPath()
        self.__readConfig()

    def __getAppPath(self):
        # determine if application is running as a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        return application_path

    def __getConfigPath(self):
        application_path = self.__getAppPath()
        return os.path.join(application_path, self.__CONFIG_FILE)

    def __readConfig(self):
        # try:
            extension = os.path.splitext(self.__CONFIG_FILE)[1]
            f = open(self.__CONFIG_PATH,"r")

            if extension == '.ini':
                config = ConfigParser()
                self.__config = config.read(self.__CONFIG_PATH)
            elif extension == '.json':
                self.__config = json.load(f)
            elif extension == '.yml':
                self.__config = yaml.safe_load(f)
            else:
                raise Exception('Not expected file extension. Use .ini|.json|.yml instead.')
        # except FileNotFoundError:
        #     pass
        # except JSONDecodeError:
        #     pass
        # except yaml.scanner.ScannerError:
        #     pass
        # except yaml.parser.ParserError:
        #     pass

    @classmethod
    def GetConfig(cls):
        return cls.__config

    @classmethod
    def GetValue(cls, key):
        return cls.__config.get(key)

