""" tunl.actions
"""
import os
import demjson

from tunl import util
from tunl.util import report, require_tunnel, qlocal, die
from tunl.data import TUNL_DIR, SYSTEM_USER, TUNL_CONFIG
from tunl.python import opj, ope
from tunl.schema import Entry

CONNECT_CMD_T = 'ssh {ident} -M -S {sock} -fnNT -L {local_port}:localhost:{remote_port} {user}@{host}'

def get_socket(nick):
    """ returns a path to the socketfile for the named tunnel """
    return opj(TUNL_DIR, nick)

def get_user(tunnel):
    """ returns the user specified by the tunnel configuration,
        and that's not specified defaults to the current system user
    """
    return tunnel.get('user', SYSTEM_USER)

def get_tunnel(nick, api=False):
    """ """
    config = util.load_config()
    require_tunnel(config, nick, api=api)
    return config[nick]

def _tunnel_status_helper(nick, api=False):
    assert nick
    status = 'up' if ope(get_socket(nick)) else 'down'
    if not api:
        report(status)
    return status

def do_status(nick, api=False):
    if not nick or nick=='all':
        # no argument implies retrieving status for each tunnel
        result = util.load_config().copy()
        for nick in result:
            result[nick] = _tunnel_status_helper(nick, api=True)
    else:
        result = {nick : _tunnel_status_helper(nick, api=api)}
    if not api:
        for nick,status in result.items():
            report("{0}: {1}".format(nick,status))
    return result

def do_list(api=False):
    """ """
    config = util.load_config().copy()
    for nick in config:
        status = _tunnel_status_helper(nick, api=True)
        config[nick].update(status=status)
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
    assert isinstance(data, dict)
    from tunl.schema import TunlEntry
    TunlEntry(data)
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
    """ starts the named tunnel"""
    tunnel = get_tunnel(nick)
    ident = tunnel.get('key', '')
    if ident:
        ident = os.path.expanduser(ident)
        if not os.path.exists(ident):
            err = "Key specified for tunnel {0} does not exist: {1}"
            err = err.format(nick, ident)
            raise SystemExit(err)
        ident = '-i "{0}"'.format(ident)
    report.start(nick)
    socket_file = get_socket(nick)
    if ope(socket_file):
        report.start("socket already exists")
        return False
    user = get_user(tunnel)
    connect_cmd = CONNECT_CMD_T.format(
        ident=ident,
        sock=socket_file,
        local_port=tunnel['local_port'],
        remote_port=tunnel['remote_port'],
        user=user,
        host=tunnel['remote_host'])
    report(connect_cmd)
    print qlocal(connect_cmd)
    return True

def do_stop(nick, api=False):
    """ stops a named tunnel which was created by do_start()

        returns True if shutdown was successful,

        return False if shutdown failed or if shutdown was unnecessary.
    """
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
