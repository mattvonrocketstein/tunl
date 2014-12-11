""" tunl
"""
import os, sys

import argparse
import demjson

from .version import __version__
from .schema import TunlSchema
from .util import report, die, require_tunnel, load_config
from .parsing import parse_argv, get_parser
from .data import HOME,TUNL_DIR, TUNL_CONFIG,VERBOSE
from .python import ope, opj, mkdir

def ensure_config():
    if not ope(TUNL_DIR):
        report("{0} does not exist, creating it".format(TUNL_DIR))
        mkdir(TUNL_DIR)
    if not ope(TUNL_CONFIG):
        report("{0} does not exist, creating it".format(TUNL_CONFIG))
        with open(TUNL_CONFIG, 'w') as fhandle:
            fhandle.write(TunlSchema.__doc__)
        ensure_config()
    else:
        data = load_config()
        TunlSchema()(data)
        report("config found and validated: {0}".format(TUNL_CONFIG))
