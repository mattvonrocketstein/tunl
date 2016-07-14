# -*- coding: utf-8 -*-
""" tunl.data
"""
import os
opj = os.path.join

HOME = os.environ['HOME']
SYSTEM_USER = os.environ['USER']
TUNL_DIR = opj(HOME, '.tunl')
TUNL_CONFIG = opj(TUNL_DIR, 'config.json')
VERBOSE = False
