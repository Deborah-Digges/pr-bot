"""
    A thin wrapper for ConfigParser
"""

from ConfigParser import SafeConfigParser


class Config:

    def __init__(self, propertyFileName):
        self.parser = SafeConfigParser()
        self.parser.read(propertyFileName)

    def getProperty(self, section, property):
        return self.parser.get(section, property)

    def getBoolean(self, section, property):
        return self.parser.getboolean(section, property)
