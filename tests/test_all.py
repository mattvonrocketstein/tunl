""" tunl/tests/test_all
"""
import sys
from unittest import TestCase
from mock import patch

from tunl import api

FAKE_CONFIG = {
  "test_tunnel_name" : {
      "local_port" : 1234,
      "remote_host" : "test_remote_host",
      "remote_port" : 4321
    }
}

@patch('tunl.util.load_config',lambda *args, **kargs: FAKE_CONFIG)
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

    def test_api_list(self):
        self.assertEqual(api.list_tunnels(), FAKE_CONFIG)
    def test_api_stop(self):
        try:
            api.stop_tunnel('doesnt_exist')
        except Exception, e:
            raise Exception,type(e)


    def test_myoutput(self, capsys): # or use "capfd" for fd-level
        print ("hello")
        sys.stderr.write("world\n")
        out, err = capsys.readouterr()
        self.assertEqual(out,"hello\n")
        self.assertEqual(err , "world\n")
        print "next"
        out, err = capsys.readouterr()
        self.assertEqual( out , "next\n")
