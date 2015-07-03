#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'jesuejunior.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
LANG_EN_FEED_ATOM = TRANSLATION_FEED_ATOM % "en"

FEED_ATOM = 'feeds/atom.xml'

ARTICLE_PATHS = ['articles']

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-31167248-1"

STATIC_PATHS = ['extra/favicon.png', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME'
    }
}
