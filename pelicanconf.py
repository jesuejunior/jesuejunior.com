#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'JJ'
SITENAME = 'Jesué Junior'
SITEURL = ''

PATH = 'content'
THEME = 'themes/jj'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']
ARTICLE_URL = '{slug}'
STATIC_PATHS = ['img', 'extra/favicon.ico', 'extra/CNAME', 'extra/robots.txt',
                'extra/jesuejunior.pub']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TYPOGRIFY = True
GOOGLE_ANALYTICS = True
LOAD_CONTENT_CACHE = False
DEFAULT_METADATA = {
    'status': 'draft',
}
