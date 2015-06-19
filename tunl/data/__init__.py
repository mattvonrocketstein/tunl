""" tunl.data
"""
import os
from tunl.python import opj

HOME = os.environ['HOME']
SYSTEM_USER = os.environ['USER']
TUNL_DIR = opj(HOME, '.tunl')
TUNL_CONFIG = opj(TUNL_DIR, 'config.json')
VERBOSE = False
