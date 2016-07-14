# -*- coding: utf-8 -*-
""" tunl.data
"""
import os

HOME = os.environ['HOME']
SYSTEM_USER = os.environ['USER']
TUNL_DIR = os.path.join(HOME, '.tunl')
TUNL_CONFIG = os.path.join(TUNL_DIR, 'config.json')
