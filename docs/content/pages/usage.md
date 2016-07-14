Title: Usage
Slug: usage
sortorder: 3
Authors: mvr

[TOC]

| command | description |
|---------|-------------|
| tunl edit    | edit ~/.tunl/config using $EDITOR |
| tunl version | show tunl version information |
| tunl help    | show CLI help |
| tunl --help    | show CLI help |
| tunl list | list all known tunnel information |
| tunl status | show status info for all tunnels |
| tunl status TUNNEL_NAME | show status info for named tunnel |
| tunl start TUNNEL_NAME | start named tunnel |
| tunl stop TUNNEL_NAME | stop named tunnel |

To add a new tunnel with the given name and data to ~/.tunl configuration try something like this:

    $ export DATA="{remote_host:'remote_host', remote_port:123, local_port:123,}"
    $ tunl add TUNNEL_NAME --data "$DATA"
