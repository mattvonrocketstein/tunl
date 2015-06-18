USAGE
=====

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
