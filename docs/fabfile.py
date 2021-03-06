# -*- coding: utf-8 -*-
import os
import shutil
import webbrowser

from fabric import api
from fabric import colors

PORT = 8000
# Assumes this documention is in src_root/docs/
PROJECT_NAME = os.path.split(os.path.dirname(os.path.dirname(__file__)))[-1]
DOC_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(DOC_ROOT)
GEN_PATH = os.path.join(DOC_ROOT, PROJECT_NAME)
DEPLOY_PATH = "~/code/ghio/{0}".format(PROJECT_NAME)
DEPLOY_PATH = os.path.expanduser(DEPLOY_PATH)


def check_links_prod():
    return check_links(
        # proto='https',
        base_domain='mattvonrocketstein.github.io')


def check_links(url='/tunl', proto='http', base_domain="localhost"):
    """ check the links wget.  """
    base_url = '{1}://{0}:'.format(base_domain, proto)
    port = str((PORT if base_domain == 'localhost' else 80))
    url = base_url + port + url
    cmd = (
        "webcheck --force "
        "--ignore-robots --avoid-external "
        "--output webcheck ")
    cmd = cmd + url
    api.local(cmd)
    webbrowser.open("file://{0}/badlinks.html".format(
        os.path.join(os.path.dirname(__file__), 'webcheck/')))
    return

    def parse_lines(lines):
        print colors.red('broken links:')
        links = [x.replace(url, '')[1:] for x in lines]
        for link in links:
            print colors.red(link)
            with api.quiet():  # (hide="warn_only=True):
                cmd = "find {0} -name *.md|xargs grep '{1}'"
                z = api.local(
                    cmd.format(DOC_ROOT, link),
                    capture=True)
                if z.succeeded:
                    print str(z)
                else:
                    print "could not find any mention"
            print
    # fab run should already be started
    logfile = "link_check.log"
    base_url = 'http://{0}:'.format(base_domain)
    port = str((PORT if base_domain == 'localhost' else 80))
    url = base_url + port + url
    wipe_logfile = lambda: api.local('rm -f "{0}"'.format(logfile))
    wipe_logfile()
    with api.settings(warn_only=True):
        api.local(
            ("wget -e robots=off --spider -r -nd "
             "-nv -o {1}  {0}").format(url, logfile))
    with open(logfile, 'r') as fhandle:
        lines = [x.strip() for x in fhandle.readlines()]
    start = end = None
    for line in lines:
        if line.startswith('Found') and line.endswith(" broken links."):
            start = lines.index(line)
        if line.startswith('FINISHED') and line.endswith('--'):
            end = lines.index(line)
    if start is not None and end is not None:
        lines = lines[start + 2:end - 1]
        parse_lines(lines)
    else:
        print "no broken links found"


def report(msg):
    print colors.red(msg)


def add_coverage(_dir=GEN_PATH):
    report("adding coverage data")
    cdir = os.path.join(SRC_ROOT, 'htmlcov')
    if os.path.exists(cdir):
        api.local("cp -rfv {0} {1}".format(cdir, _dir))
    else:
        report("coverage directory does not exist: {0}".format(cdir))


def clean():
    """ Remove generated files """
    if os.path.isdir(GEN_PATH):
        shutil.rmtree(GEN_PATH)
        os.makedirs(GEN_PATH)


def build(conf='pelicanconf.py'):
    """Build local version of site"""
    with api.lcd(os.path.dirname(__file__)):
        api.local('pelican -s {0} -o {1}'.format(conf, GEN_PATH))


def rebuild():
    """`clean` then `build`"""
    clean()
    build()
    add_coverage(GEN_PATH)


def regenerate():
    """Automatically regenerate site upon file modification"""
    add_coverage()
    with api.lcd(os.path.dirname(__file__)):
        api.local('pelican -r -s pelicanconf.py -o {0}'.format(GEN_PATH))


def serve():
    """Serve site at http://localhost:8000/"""
    with api.lcd(os.path.dirname(GEN_PATH)):
        api.local("twistd -n web -p {0} --path .".format(PORT))


def push():
    if os.path.exists(DEPLOY_PATH):
        with api.lcd(DEPLOY_PATH):
            cmd = "find . -type f|"
            cmd += "xargs --no-run-if-empty git rm -f"
            api.local(cmd)
    api.local("mkdir -p {0}".format(DEPLOY_PATH))
    api.local(
        "cp -rfv {0} {1}".format(
            os.path.join(GEN_PATH, '*'),
            DEPLOY_PATH))
    with api.lcd(DEPLOY_PATH):
        api.local("find . -type f|xargs --no-run-if-empty git add")
        api.local("git commit . -m'publishing {0}'".format(PROJECT_NAME))
        api.local("git push")


def publish():
    build_prod()
    push()


def build_prod():
    clean()
    build("pelican_publish.py")
    add_coverage(GEN_PATH)


def run():
    from littleworkers import Pool
    commands = ['fab regenerate', 'fab serve']
    pool = Pool(workers=2)
    pool.run(commands)
