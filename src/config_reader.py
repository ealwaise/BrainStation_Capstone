'''
This module is for reading file paths from a configuration file titled
'config.ini' located up one level from the location of this module. It contains
the following functions:

get_value - Reads a single value from a configuration file.
get_path - Reads a file path from a configuration file.
'''
from configparser import ConfigParser
import os

def get_value(section, key):
    '''
    Gets the value from the input section and key in config.ini.
    
    Arguments
    ---------
    section - str
        A section in config.ini.
    key - str
        A key in config.ini
    
    Returns
    -------
    value - str
        The value corresponding to the input section and key.
    '''
    config = ConfigParser()
    config.read('../../config.ini')
    value = config.get(section, key)
    
    return value
    
def get_path(key):
    '''Gets a file path corresponding to the input key.
    
    Arguments
    ---------
    key - str
        A key in config.ini, assumed to be in the 'PATHS' section. The
        corresponding value is assumed to be a commma-separated list of
        folders/filenames.
        
    Returns
    -------
    path - str
        The desired file path.
    '''
    dirs = get_value('PATHS', key).split(",")
    path = os.path.join(*dirs)
    
    return path