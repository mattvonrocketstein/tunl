""" tunl.bin._tunl
"""
from tunl import ensure_config, parse_argv

def main():
    ensure_config()
    parse_argv()

if __name__=='__main__':
    main()
