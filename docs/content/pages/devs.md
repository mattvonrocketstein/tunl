Title: Dev
Slug: dev
sortorder: 5
Authors: mvr

[TOC]

## Programmatic Usage

     >>> from tunl import api
     >>> api.list_tunnels()
     {'mongo': {'local_port': 27000,
      'remote_host': 'host',
      'remote_port': 27017,
      'status': 'down',
      'user': 'admin'},
     'jenkins': {'key': '~/.ssh/key.pem',
      'local_port': 8081,
      'remote_host': 'jenkins',
      'remote_port': 8080,
      'status': 'down',
      'user': 'ubuntu'}}
     >>> start_success = api.start_tunnel('mongo')
    tunl: ssh  -M -S /home/vagrant/.tunl/mongo -fnNT -L 27000:localhost:27017 admin@host
     >>> print start_success
     True
