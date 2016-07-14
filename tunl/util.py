# -*- coding: utf-8 -*-
""" tunl.util
"""
import os
import demjson

from report import Reporter
from .schema import TunlSchema
from .data import (
    TUNL_CONFIG, TUNL_DIR, DEFAULT_DATA)
ope = os.path.exists
report = Reporter("tunl")


class TunnelConfigurationError(ValueError):
    pass


def load_config():
    """ """
    ensure_config()
    with open(TUNL_CONFIG) as fhandle:
        data = demjson.decode(fhandle.read())
    return data


def die(msg):
    """ """
    report.error(msg)
    raise SystemExit(1)


def require_tunnel(config, nick, api=False):
    """ """
    if nick not in config:
        err = "no such tunnel {0}, are you using the right nickname?\n\n{1}"
        err = err.format(nick, config.keys())
        if not api:
            die(err)
        else:
            raise TunnelConfigurationError(err)


def qlocal(cmd):
    """ """
    return os.system(cmd)


def ensure_config():
    if not ope(TUNL_DIR):
        report("tDEFAULTunl config dir \"{0}\" does not exist, creating it".format(
            TUNL_DIR))
        os.mkdir(TUNL_DIR)
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
