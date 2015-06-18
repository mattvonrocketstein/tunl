Configuration
=============

Configuration is stored in `~/.tunl/config.json`, which is created if it does not exist already.  The format is basically `{tunnel_name : {..tunnel_info..}, .. }`.  For the tunnel info, the keys `remote_host`, `remote_port` and `local_port` are required. Two other JSON entries are optional: `user`, and `key`.  As you would expect, `user` simply refers to the remote ssh user to login as, and defaults to the current (local) user.  The `key` entry refers to an ssh key/ident file, which is used in the tunnel invocation as an argument to `ssh -i`.  See the example below.

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
