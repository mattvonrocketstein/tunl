""" tunl.api
"""
from tunl import actions

def gen_method(name):
    def newf(*args, **kargs):
        assert 'api' not in kargs
        kargs.update(api=True)#
        fxn = getattr(actions,name)
        return fxn(*args, **kargs)
    return newf

stop_tunnel = gen_method('do_stop')
start_tunnel = gen_method('do_start')
add_tunnel = gen_method('do_add')
