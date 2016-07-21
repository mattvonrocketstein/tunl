# -*- coding: utf-8 -*-
""" tunl.util
"""
import os
from functools import wraps

import demjson
from report import Reporter

from .schema import TunlSchema, DEFAULT_DATA
from .data import TUNL_CONFIG, TUNL_DIR

ope = os.path.exists
report = Reporter("tunl")


class TunnelConfigurationError(ValueError):
    pass


def load_config():
    """ """
    with open(TUNL_CONFIG) as fhandle:
        data = demjson.decode(fhandle.read())
    return data


def require_config(fxn):
    @wraps(fxn)
    def newf(*args, **kargs):
        ensure_config()
        return fxn(*args, **kargs)
    return newf


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


def ensure_config(force=False):
    """ """
    if ensure_config.config_ensured and not force:
        return
    if not os.path.exists(TUNL_DIR):
        report("tunl config dir \"{0}\" does not exist, creating it".format(
            TUNL_DIR))
        os.mkdir(TUNL_DIR)
    if not os.path.exists(TUNL_CONFIG):
        report("tunl config \"{0}\" does not exist, creating it".format(
            TUNL_CONFIG))
        with open(TUNL_CONFIG, 'w') as fhandle:
            fhandle.write(DEFAULT_DATA)
        ensure_config()
    else:
        data = load_config()
        TunlSchema(data)
        report("config found and validated: {0}".format(TUNL_CONFIG))
    ensure_config.config_ensured = True
ensure_config.config_ensured = False
