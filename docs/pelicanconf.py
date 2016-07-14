#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pelican configuration for tunl docs
#
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.dirname(__file__))

PORT = 8001
AUTHOR = u'mvr'
SITENAME = 'tunl'

SITEURL = 'http://localhost:{0}/tunl'.format(PORT)
RELATIVE_URLS = False

PATH = os.path.join(os.path.dirname(__file__), 'content')

TIMEZONE = 'America/New_York'
THEME = "theme"
STATIC_PATHS = ["images", 'js']
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True
MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'admonition',
    'tables', 'toc', 'wikilinks'
]
PLUGIN_PATHS = ["."]
PLUGINS = [
    'extract_toc',
    'simple_footnotes',
]

LINKS = (
    ('Source code', 'https://github.com/mattvonrocketstein/tunl/'),
    ('Issues', 'https://github.com/mattvonrocketstein/tunl/issues'),
)

# Social widget
SOCIAL = tuple()
IGNORE_FILES = ['.#*']
DEFAULT_PAGINATION = False
LOAD_CONTENT_CACHE = False
