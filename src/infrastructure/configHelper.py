
import os
import sys
import json

from infrastructure.singleton import singleton

class ConfigKeys:
    ENABLE_THEME = "EnableTheme"
    LOGIN_USER = "User"
    LOGIN_PASSWORD = "Password"

@singleton
class ConfigHelper:
    __CONFIG_FILE = 'config.json'

    __config = dict()

    def __init__(self):
        application_path = self.__getAppPath()
        configPath = os.path.join(application_path, self.__CONFIG_FILE)
        self.__readConfig(configPath)

    def __getAppPath(self):
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        return application_path

    def __readConfig(self, configPath):
        with open(configPath,"r") as f:
            self.__config = json.load(f)


    @classmethod
    def GetConfig(cls):
        return cls.__config

    @classmethod
    def GetValue(cls, key):
        return cls.__config.get(key)

