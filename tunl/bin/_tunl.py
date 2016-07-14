# -*- coding: utf-8 -*-
""" tunl.bin._tunl
"""
from tunl.util import ensure_config
from tunl.parsing import parse_argv


def main():
    ensure_config()
    parse_argv()

if __name__ == '__main__':
    main()
