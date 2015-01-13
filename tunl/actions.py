""" tunl.actions
"""
import demjson

from tunl import util
from tunl.util import report, require_tunnel, qlocal, die
from tunl.data import TUNL_DIR, SYSTEM_USER, TUNL_CONFIG
from tunl.python import opj, ope
from tunl.schema import Entry

def get_socket(nick):
    """ """
    return opj(TUNL_DIR, nick)

def get_user(tunnel):
    """ """
    return tunnel.get('user', SYSTEM_USER)

def get_tunnel(nick, api=False):
    """ """
    config = util.load_config()
    require_tunnel(config, nick, api=api)
    return config[nick]

def do_status(nick, api=False):
    status = 'up' if ope(get_socket(nick)) else 'down'
    if not api:
        report(status)
    return status

def do_list(api=False):
    """ """
    config = util.load_config()
    for nick in config:
        config[nick].update(status=do_status(nick))
    if api:
        return config
    else:
        report("")
        for t in config:
            print '  {0}: '.format(t)
            for x, y in config[t].items():
                print '    {0}: {1}'.format(x,y)

def do_add(nick='', data={}, api=False, force=False):
    """ """
    config = util.load_config()
    assert isinstance(nick, basestring) and nick
    if isinstance(data, basestring):
        data = demjson.decode(data)
    assert isinstance(data, dict) and data
    if nick in config and not force:
        err = "{0} is already present in {1}"
        err = err.format(nick, TUNL_CONFIG)
        if api:
            raise ValueError(err)
        else:
            return die(err)
    Entry(data)
    config[nick] = data
    config = demjson.encode(config, compactly=False)
    with open(TUNL_CONFIG, 'w') as fhandle:
        fhandle.write(config)
    if not api:
        report("rewrote config: ")
        print config
    return config

def do_start(nick, api=False):
    """ """
    tunnel = get_tunnel(nick)
    report.start(nick)
    socket_file = get_socket(nick)
    if ope(socket_file):
        report.start("socket already exists")
        return False
    connect_cmd_t = 'ssh -M -S {0} -fnNT -L {1}:localhost:{2} {3}@{4}'
    user = get_user(tunnel)
    connect_cmd = connect_cmd_t.format(
        socket_file, tunnel['local_port'], tunnel['remote_port'],
        user,
        tunnel['remote_host'])
    report(connect_cmd)
    print qlocal(connect_cmd)
    return True

def do_stop(nick, api=False):
    """ stops the tunnel created by do_start() """
    tunnel = get_tunnel(nick, api=api)
    tunnel_user = get_user(tunnel)
    socket_file = get_socket(nick)
    if not ope(socket_file):
        report("no socket file found.  probably the tunnel is down already")
        return False
    shutdown_cmd_t = 'ssh -S {0} -O exit {1}'
    shutdown_cmd = shutdown_cmd_t.format(socket_file, tunnel_user)
    report(shutdown_cmd)
    qlocal(shutdown_cmd)
    return True
