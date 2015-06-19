""" tunl
"""
import os, sys

import argparse
import demjson

from .version import __version__
from .schema import TunlSchema, DEFAULT_DATA
from .util import report, die, require_tunnel, load_config
from .parsing import parse_argv, get_parser
from .data import HOME, TUNL_DIR, TUNL_CONFIG,VERBOSE
from .python import ope, opj, mkdir

def ensure_config():
    if not ope(TUNL_DIR):
        report("tunl config dir \"{0}\" does not exist, creating it".format(
            TUNL_DIR))
        mkdir(TUNL_DIR)
    if not ope(TUNL_CONFIG):
        report("tunl config \"{0}\" does not exist, creating it".format(
            TUNL_CONFIG))
        with open(TUNL_CONFIG, 'w') as fhandle:
            fhandle.write(DEFAULT_DATA)
        ensure_config()
    else:
        data = load_config()
        TunlSchema(data)
        report("config found and validated: {0}".format(TUNL_CONFIG))
