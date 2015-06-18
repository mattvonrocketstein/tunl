[about](#about) | [installation](#installation) | [usage](#usage) | [testing](#testing) |


<a name="about">ABOUT</a>
=========================
Tunl is a dead-simple tunnel manager.  I wrote this mainly because I wanted both command-line and programmatic access to a ssh-tunnel manager with simple configuration files.  (Also I can't be bothered to remember the difficult command line syntax, and I hate typing.)

<a name="installation">INSTALLATION</a>
=======================================

```shell
   $ git clone https://github.com/mattvonrocketstein/tunl.git
   $ cd tunl
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   $ python setup.py develop
```
