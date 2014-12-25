""" tunl.util
"""
import demjson

from report import Reporter
from .data import TUNL_CONFIG

report = Reporter("tunl")

def load_config():
    with open(TUNL_CONFIG) as fhandle:
        data = demjson.decode(fhandle.read())
    return data

def die(msg):
    report.error(msg)
    raise SystemExit(1)

def require_tunnel(config, nick):
    if nick not in config:
        err = "no such tunnel {0}, are you using the right nickname?\n\n{1}"
        err = err.format(nick, config.keys())
        die(err)

def qlocal(cmd):
    import os
    os.system(cmd)
