""" tunl/tests/test_bin_tunl
"""
import os, sys
from unittest import TestCase
from mock import patch

from tunl.bin._tunl import entry

class TestCommandLineEntry(TestCase):
    def test_tunl_cli(self):
        self.assertRaises(SystemExit, entry)
