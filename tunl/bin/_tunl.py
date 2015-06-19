""" tunl.bin._tunl
"""
from tunl import ensure_config, parse_argv

def main():
    ensure_config()
    parse_argv()
entry = main

if __name__=='__main__':
    main()
