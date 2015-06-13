""" tunl/tests/__init__
"""
import os
import warnings, tempfile
if not os.environ.get('HOME'):
    warnings.warn('$HOME is not set!  using /tmp')
    os.environ.get('HOME', tempfile.gettempdir())
