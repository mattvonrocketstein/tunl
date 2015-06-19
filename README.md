## About tunl

Tunl is a ssh-tunnel manager without a lot of frills.  It has a command-line interface which works any place you have ssh and python.  I wrote this mainly because I wanted dead simple command-line and programmatic access to a ssh-tunnel manager with unsurprising configuration files.  (Also I can't be bothered to remember the ssh command line syntax, and I sure do hate typing)

[The main documentation is located here.](http://mattvonrocketstein.github.io/tunl/)

## Installing tunl

Install with pypi:

```shell
   $ pip install tunl
```

Or try the bleeding edge:

```shell
   $ git clone https://github.com/mattvonrocketstein/tunl.git
   $ cd tunl
   $ virtualenv venv
   $ source venv/bin/activate
   $ python setup.py develop
```
