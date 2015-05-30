[about](#about) | [installation](#installation) | [usage](#usage) | [testing](#testing) |


<a name="about">ABOUT</a>
=========================
Tunl is a dead-simple tunnel manager.  I wrote this mainly because I wanted both command-line and programmatic access to a ssh-tunnel manager with simple configuration files.  (Also I can't be bothered to remember the difficult command line syntax, and I hate typing.)

<a name="installation">INSTALLATION</a>
=======================================

```shell
  $ git clone https://github.com/mattvonrocketstein/tunl.git
  $ pip install -r requirements.txt
  $ python setup.py install
```

<a name="config">Configuration</a>
==================================
Configuration is stored in `~/.tunl/config.json`, which is created if it does not exist already.  The format is basically `{tunnel_name : {..tunnel_info..}, .. }`.  For the tunnel info, the keys `remote_host`, `remote_port` and `local_port` are required but `user` is optional and defaults to the current user.  Another optional See the example below.

```json
{
  "my_simple_tunnel" : {
      "local_port" : 123,
      "remote_host" : "remote_host",
      "remote_port" : 123
    }
  "another_more_complex_tunnel" : {
      "local_port" : 27000,
      "remote_host" : "some.remote.host.org",
      "remote_port" : 27017,
      "user" : "some_guy",
      "key"  : "some_path_to_ssh_key.pem",
    },
}
```

<a name="usage">USAGE</a>
==========================

To add a new tunnel:

```shell
tunl tunnel_name --add "{remote_host:'remote_host', remote_port:123, local_port:123,}"
```
To start/stop a tunnel:

```shell
tunl tunnel_name --start
tunl tunnel_name --stop
```

To show tunnel status:

```shell
tunl tunnel_name --status
```

To list all tunnel information and status:

```shell
tunl --list
```

To edit tunnel config with $EDITOR:

```shell
tunl --edit
```


<a name="testing">TESTING</a>
=============================

```shell
  $ virtualenv venv_tunl
  $ source venv_tunl/bin/activate
  $ pip install -r requirements.txt
  $ python setup.py install
  $ pip install tox
  $ tox
```
