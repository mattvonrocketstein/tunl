""" tunl.parsing
"""
import sys
import argparse

from .util import report, die
from .actions import do_list, do_start, do_stop, do_add, do_status

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', action="store_true", default=False)
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    parser.add_argument('--start', action="store_true", default=False)
    parser.add_argument('--add', default="")
    parser.add_argument('--stop', action="store_true", default=False)
    parser.add_argument('--status', action="store_true", default=False)
    return parser

def parse_argv():
    parser = get_parser()
    args, unknown = parser.parse_known_args(sys.argv[1:])
    if len(vars(args)):
        report("parsed argv: "+str([args,unknown]))

    # enforce no arg given with --list
    if len(unknown)>1:
        err = 'maximum of one argument, got {0}'.format(unknown)
        die(err)

    if args.list and unknown:
        err = 'no arguments should be given with --list'

    # enforce maximum of one: list|start|stop|status
    count = sum([(1 if x else 0) for x in [
        args.list, args.add,
        args.start, args.stop,
        args.status]])

    err = 'specify only one of add|list|start|stop|status'
    if count > 1:
        die(err)

    if args.list:
        do_list()
        return

    try:
        nick = unknown[0]
    except IndexError:
        do_list()
        return
    if args.start:
        do_start(nick)
    elif args.add:
        data = args.add
        do_add(nick, data)
    elif args.stop:
        do_stop(nick)
    elif args.status:
        do_status(nick)
