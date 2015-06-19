#!/usr/bin/env python
""" setup.py for tunl
"""
import os, sys
from setuptools import setup, find_packages

# make sure that finding packages works, even
# when setup.py is invoked from outside this dir
this_dir = os.path.dirname(os.path.abspath(__file__))
if not os.getcwd()==this_dir:
    os.chdir(this_dir)

# make sure we can import the version number so that it doesn't have
# to be changed in two places. tunl/__init__.py is also free
# to import various requirements that haven't been installed yet
sys.path.append(os.path.join(this_dir, 'tunl'))
from version import __version__
sys.path.pop()

base_url = 'https://github.com/mattvonrocketstein/tunl/'

install_requires = [
    'argparse',
    'demjson',
    'pygments',
    'reporting',
    'voluptuous',
    ]

packages = [x for x in find_packages() if x not in ['tests']]
description = ('lightweight shh tunnel management utility.  '
               'supports command-line and programmatic usage')
setup(
    name         = 'tunl',
    version      = __version__,
    description  = description,
    author       = 'mattvonrocketstein',
    author_email = '$author@gmail',
    url          = base_url,
    download_url = base_url + '/tarball/master',
    packages     = packages,
    keywords     = ['ssh','tunnel','manager'],
    entry_points = {
        'console_scripts': \
        ['tunl = tunl.bin._tunl:main', ] },
    install_requires = install_requires,)
