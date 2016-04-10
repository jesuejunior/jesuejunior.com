#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JJ'
SITENAME = u'Jesué Junior'
SITEURL = ''

PATH = 'content'

THEME = 'themes/jj'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['articles']
ARTICLE_URL = '{slug}'
STATIC_PATHS = ['img', 'extra/favicon.png', 'extra/CNAME', 'extra/robots.txt']


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "backreftranslate"]

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'weekly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
}

TYPOGRIFY = True

GOOGLE_ANALYTICS = True

LOAD_CONTENT_CACHE = False
