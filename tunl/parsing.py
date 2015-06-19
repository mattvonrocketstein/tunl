""" tunl.parsing
"""
import os, sys
import demjson
import argparse
import voluptuous
from report import console
from .data import TUNL_CONFIG
from .util import report, die
from .actions import do_list, do_start, do_stop, do_add, do_status
from tunl import version

def get_parser():
    descr = ''
    epilog = ''
    parser = argparse.ArgumentParser(description=descr, epilog=epilog)
    parser.add_argument(
        "-v", '--version', default=False, dest='version',
        action='store_true',
        help=("show version information"))
    subparsers = parser.add_subparsers(help='commands')

    help_parser = subparsers.add_parser('help', help='show help info')
    help_parser.set_defaults(subcommand='help')

    version_parser = subparsers.add_parser(
        'version', help='show tunl version')
    version_parser.set_defaults(subcommand='version')

    list_parser = subparsers.add_parser(
        'list', help='list known tunnels')
    list_parser.set_defaults(subcommand='list')

    status_parser = subparsers.add_parser(
        'status', help='show tunnel status information')
    status_parser.set_defaults(subcommand='status')
    status_parser.add_argument(
        'tunnel_name', nargs='?', default='',
        help=("status for the named tunnel"))

    edit_parser = subparsers.add_parser(
        'edit', help='edit tunl config')
    edit_parser.set_defaults(subcommand='edit')

    start_parser = subparsers.add_parser(
        'start', help='start the named tunnel')
    start_parser.set_defaults(subcommand='start')
    start_parser.add_argument(
        'tunnel_name', default=os.getcwd(),
        help=("start the named tunnel"))

    stop_parser = subparsers.add_parser(
        'stop', help='stop the named tunnel')
    stop_parser.set_defaults(subcommand='stop')
    stop_parser.add_argument(
        'tunnel_name', default=os.getcwd(),
        help=("stop the named tunnel"))
    add_parser = subparsers.add_parser(
        'add', help='add new tunnel to configuration')
    add_parser.set_defaults(subcommand='add')
    add_parser.add_argument(
        'tunnel_name', default='',
        help=("name for the new tunnel"))
    add_parser.add_argument(
        '--data', dest='tunnel_json',
        metavar='JSON_DATA', default='',
        help=("ports, host, and username information for the new tunnel"))
    return parser

def parse_argv():
    parser = get_parser()
    args, unknown = parser.parse_known_args(sys.argv[1:])
    if args.subcommand in ['version', 'help']:
        if args.subcommand == 'version':
            print version.__version__
        if args.subcommand == 'help':
            parser.print_help()
        raise SystemExit()
    elif args.subcommand == 'list':
        do_list()
    elif args.subcommand == 'status':
        do_status(args.tunnel_name)
    elif args.subcommand == 'edit':
        ed = os.environ.get('EDITOR', 'vi')
        report('opening configuration in {0}'.format(ed))
        os.system(ed + ' ' + TUNL_CONFIG)
    elif args.subcommand == 'start':
        do_start(args.tunnel_name)
    elif args.subcommand == 'stop':
        do_stop(args.tunnel_name)
    elif args.subcommand == 'add':
        data = args.tunnel_json
        err = console.red('Bad data passed into "tunl add" command.  ')
        err += (
            'Example usage follows:\n   '
            'tunl add tunl_name --data "'
            "{remote_host:'monkey.org', local_port:5151, remote_port:22}"
            '"')
        if not data:
            raise SystemExit(err)
        try:
            data = demjson.decode(data)
        except demjson.JSONDecodeError,e:
            print "demjson.JSONDecodeError: " + str(e)
            raise SystemExit(err)
        else:
            try:
                do_add(args.tunnel_name, data)
            except voluptuous.Invalid, e:
                print "voluptuous.Invalid: " + str(e)
                raise SystemExit(err)

    else:
        err = 'unrecognized subcommand "{0}"'
        raise SystemExit(err.format(args.subcommand))
