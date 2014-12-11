#!/usr/bin/env python
#
# fabfile for pkg_name
#
# this file is a self-hosting fabfile, meaning it
# supports direct invocation with standard option
# parsing, including --help and -l (for listing commands).
#
# summary of commands/arguments:
#
#   * fab pypi_repackage: update this package on pypi
#
import os
import sys
from fabric.colors import red
from fabric.api import lcd, local
from fabric.contrib.console import confirm

_ope = os.path.exists
_mkdir = os.mkdir
_expanduser = os.path.expanduser
_dirname = os.path.dirname

def pypi_repackage():
    ldir = _dirname(__file__)
    print red("warning:") + (" by now you should have commited local"
                             " master and bumped version string")
    ans = confirm('proceed with pypi update in "{0}"?'.format(ldir))
    if not ans: return
    with lcd(ldir):
        local("git checkout -b pypi") # in case this has never been done before
        local("git checkout pypi")
        local("git reset --hard master")
        local("python setup.py register -r pypi")
        local("python setup.py sdist upload -r pypi")

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
    from fabric.main import main as fmain
    patched_argv = ['fab', '-f', __file__,] + \
                   sys.argv[sys.argv.index(__file__)+1:]
    sys.argv = patched_argv
    fmain()
