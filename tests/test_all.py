""" tunl/tests/test_all
"""
from unittest import TestCase

class TestTunl(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        from tunl.version import __version__
        self.assertTrue(isinstance(__version__, float))

    def test_data(self):
        # maybe assert that there are no other modules
        # in the namespace? other than that there is not
        # much to do.  just make sure the import isn't broken
        exec('from tunl.data import *')

    def test_2(self):
        pass
import sys
def test_myoutput(capsys): # or use "capfd" for fd-level
    print ("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print "next"
    out, err = capsys.readouterr()
    assert out == "next\n"
