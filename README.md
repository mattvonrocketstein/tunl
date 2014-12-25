[about](#about) | [installation](#installation) | [usage](#usage) | [testing](#testing) |


<a name="about">ABOUT</a>
=========================
Tunl is a dead-simple tunnel manager.  I wrote this mainly because I wanted both command-line and programmatic access to a ssh-tunnel manager with simple configuration files.  (Also I can't be bothered to remember the difficult command line syntax, and I hate typing.)

<a name="installation">INSTALLATION</a>
=======================================

```shell
  $ git clone https://github.com/mattvonrocketstein/tunl.git
  $ step2
```

<a name="config">Configuration</a>
==================================
Configuration is stored in `~/.tunl/config.json`, which is created if it does not exist already.  The format is basically `{tunnel_name : tunnel_info}`.  For the tunnel info `remote_host`, `remote_port` and `local_port` are required but `user` is optional and defaults to the current user.  See the example below.

```json
{
  "mongo" : {
      "local_port" : 27000,
      "remote_host" : "some.remote.host.org",
      "remote_port" : 27017,
      "user" : "matt"
    },
  "tunnel_name" : {
      "local_port" : 123,
      "remote_host" : "remote_host",
      "remote_port" : 123
    }
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

<a name="testing">TESTING</a>
=============================
