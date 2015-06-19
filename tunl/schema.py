""" tunl.schema
"""

from voluptuous import Schema
from voluptuous import Required, Invalid
from voluptuous import Optional

Entry = Schema({
    Required("remote_host") : basestring,
    Required("remote_port") : int,
    Required("local_port")  : int,
    Optional("user")        : basestring,
    Optional("key")         : basestring,
    })
TunlEntry=Entry

DEFAULT_DATA = """// example configuration for tunl
{
'tunnel_nickname': {
    'local_port'   : 0,
    'remote_port'  : 0,
    'remote_host'  : 'example_host',
    'user' : 'optional_user' },
}
"""
TunlSchema = Schema({basestring:Entry})
