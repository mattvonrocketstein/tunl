""" tunl/tests/test_all
"""
import os, sys
from unittest import TestCase
from mock import patch

from tunl import api
from tunl import actions
from tunl import util
from tunl.parsing import get_parser

FAKE_CONFIG = {
  "test_tunnel_name" : {
      "local_port" : 1234,
      "remote_host" : "test_remote_host",
      "remote_port" : 4321
    }
}

@patch('tunl.util.load_config', lambda *args, **kargs: FAKE_CONFIG)
@patch('os.system', lambda *args, **kargs: None)
class TestAPI(TestCase):
    def test_api_list(self):
        self.assertEqual(api.list_tunnels(), FAKE_CONFIG)

    def test_api_stop(self):
        self.assertRaises(
            ValueError,
            lambda: api.stop_tunnel('doesnt_exist'))
        stopped = api.stop_tunnel('test_tunnel_name')
        self.assertEqual(False, stopped)

    def test_start(self):
        api.start('test_tunnel_name')

    def test_get_user(self):
        self.assertEqual(os.environ['USER'], actions.get_user(FAKE_CONFIG))

    def test_get_tunl(self):
        self.assertRaises(
            util.TunnelConfigurationError,
            lambda: actions.get_tunnel('does_not_exist', api=True))
        self.assertEqual(
            FAKE_CONFIG['test_tunnel_name'],
            actions.get_tunnel('test_tunnel_name', api=True))

import tunl
import tempfile, shutil
from tunl import data
from tunl import ensure_config
thisdir = os.path.dirname(__file__)

@patch('tunl.util.load_config', lambda *args, **kargs: FAKE_CONFIG)
class TestTunl(TestCase):

    def test_ensure_config(self):
        tunl_dir = tempfile.mkdtemp()
        tunl_config = os.path.join(tunl_dir, 'tmpfile.json')
        try:
            with patch('tunl.TUNL_DIR', tunl_dir):
                with patch('tunl.TUNL_CONFIG', tunl_config):
                    ensure_config()
            self.assertTrue(os.path.exists(tunl_config))
            self.assertTrue(os.path.exists(tunl_dir))

        finally:
            shutil.rmtree(tunl_dir)
        #self.assertEqual(data.TUNL_DIR, thatdir)

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_version(self):
        from tunl.version import __version__
        self.assertTrue(isinstance(__version__, float))

    def test_die(self):
        self.assertRaises(SystemExit,
                          lambda: util.die('error'))

    def test_data(self):
        # maybe assert that there are no other modules
        # in the namespace? other than that there is not
        # much to do.  just make sure the import isn't broken
        exec('from tunl.data import *')

    def test_cl_parser(self):
        parser = get_parser()
        self.assertEqual(
            set(parser._option_string_actions.keys()),
            set(('-h -l --add --list --start --status'
                 ' --edit --verbose --help -v --stop').split()))


    def test_schema_validator(self):
        from tunl.schema import TunlSchema
        from voluptuous import MultipleInvalid
        import demjson

        TunlSchema()({
            "test_tunnel_name" : {
                "local_port" : 1234,
                "remote_host" : "test_remote_host",
                "remote_port" : 4321
                }
            })
        self.assertRaises(
            MultipleInvalid,
            lambda: TunlSchema()({
                "test_tunnel_name" : {
                    "local_prot" : 1234,
                    "remote_hsot" : "test_remote_host",
                    "remote_port" : 4321
                    }
                }))

    def asdtest_myoutput(self, capsys): # or use "capfd" for fd-level
        print ("hello")
        sys.stderr.write("world\n")
        out, err = capsys.readouterr()
        self.assertEqual(out,"hello\n")
        self.assertEqual(err , "world\n")
        print "next"
        out, err = capsys.readouterr()
        self.assertEqual( out , "next\n")
