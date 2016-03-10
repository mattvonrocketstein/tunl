""" tunl.data
"""
import os
from .python import opj

HOME = os.environ['HOME']
XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME', opj(HOME, '.config'))
SYSTEM_USER = os.environ['USER']
TUNL_DIR = opj(XDG_CONFIG_HOME, 'tunl')
TUNL_CONFIG = opj(TUNL_DIR, 'config.json')
VERBOSE = False
