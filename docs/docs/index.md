<center><img style="border:3px solid black;" src="img/tunl.jpg" style="width:100%;opacity:0.6;filter:alpha(opacity=60);"/></center>

## About tunl

Tunl is a ssh-tunnel manager without a lot of frills.  It has a command-line interface which works any place you have ssh and python.  I wrote this mainly because I wanted dead simple command-line and programmatic access to a ssh-tunnel manager with unsurprising configuration files.  (Also I can't be bothered to remember the ssh command line syntax, and I sure do hate typing)

Tunl is written in python: see [this section](devs/) for information about using it as a library.

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
