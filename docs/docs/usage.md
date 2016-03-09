USAGE
=====

| command | description |
|---------|-------------|
| `tunl edit`    | edit ~/.tunl/config using $EDITOR |
| `tunl version` | show `tunl` version information |
| `tunl help`    | show CLI help |
| `tunl --help`    | show CLI help |
| `tunl list` | list all known tunnel information |
| `tunl status` | show status info for all tunnels |
| `tunl start` | start all tunnels |
| `tunl stop` | stop all tunnels |
| `tunl status TUNNEL_NAME ...` | show status info for named tunnel(s) |
| `tunl start TUNNEL_NAME ...` | start named tunnel(s) |
| `tunl stop TUNNEL_NAME ...` | stop named tunnel(s) |

To add a new tunnel with the given name and data to ~/.tunl configuration try something like this:

```shell
tunl add TUNNEL_NAME --data "{remote_host:'remote_host', remote_port:123, local_port:123,}"`
```
