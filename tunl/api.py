""" tunl.api
"""
from .actions import do_add

def add_tunnel(*args, **kargs):
    assert 'api' not in kargs
    kargs.update(api=True)
    return do_add(*args, **kargs)
