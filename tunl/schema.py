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
    })

class TunlSchema(Schema):
    """
    // example configuration for tunl
    {
      'tunnel_nickname': {
        'local_port'   : 0,
        'remote_port'  : 0,
        'remote_host'  : 'example_host',
        'user' : 'optional_user'
      }
    }
    """
    def config_validator(self, x):
        x = x.copy()
        for k, v in x.items():
            if not isinstance(k, basestring):
                raise Invalid("{0} is not a string".format(k))
            Entry(v)

    def __init__(self):
        super(TunlSchema, self).__init__(self.config_validator)
