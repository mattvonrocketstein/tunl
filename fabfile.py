#!/usr/bin/env python
#
# fabfile for pkg_name
#
# this file is a self-hosting fabfile, meaning it
# supports standard option parsing, including
# --help and -l (for listing commands).
#
# summary of commands/arguments:
#
#   * foo: bar, baz, qux
#
import os, re, sys

from fabric.api import env, run
from fabric.colors import red
from fabric.api import lcd, local, quiet
from fabric.contrib.console import confirm

_ope = os.path.exists
_mkdir = os.mkdir
_expanduser = os.path.expanduser

def repackage():
    local('python setup.py develop')
    ans=confirm('proceed with pypi?')
    if ans:
        #with quiet():
        local('python setup.py register -r pypi')
        local('python setup.py sdist upload -r pypi')

if __name__ == '__main__':
    # a neat hack that makes this file a "self-hosting" fabfile,
    # ie it is invoked directly but still gets all the fabric niceties
    # like real option parsing, including --help and -l (for listing
    # commands). note that as of fabric 1.10, the file for some reason
    # needs to end in .py, despite what the documentation says.  see:
    # http://docs.fabfile.org/en/1.4.2/usage/fabfiles.html#fabfile-discovery
    #
    # the .index() manipulation below should make this work regardless of
    # whether this is invoked from shell as "./foo.py" or "python foo.py"
    import sys
    from fabric.main import main as fmain
    patched_argv = ['fab', '-f', __file__,] + \
                   sys.argv[sys.argv.index(__file__)+1:]
    sys.argv = patched_argv
    fmain()
