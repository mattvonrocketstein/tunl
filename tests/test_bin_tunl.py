# -*- coding: utf-8 -*-
""" tunl/tests/test_bin_tunl
"""
import os
import sys
from unittest import TestCase
from mock import patch

from tunl.bin._tunl import main


class TestCommandLineEntry(TestCase):

    def test_tunl_cli(self):
        self.assertRaises(SystemExit, main)
