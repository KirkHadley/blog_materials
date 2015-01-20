#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Juannell Riley'
SITENAME = u'Do Nothing, Say Nothing'
SITEURL = ''
PATH = 'content'
OUTPUT_PATH = '/var/www/output'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RELATIVE_URLS = True
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME = '/home/kirk/pelican-themes/aboutwilson'  
PLUGIN_PATHS = ['/home/kirk/pelican-plugins']
PLUGINS = ['summary']
SUMMARY_END_MARKER = '<!--more-->'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
