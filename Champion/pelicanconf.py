#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Neil Williams'
SITENAME = 'Champion'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'menuorder'
# Useful config for migrating from Jekyll
# ---
# https://github.com/noirbizarre/pelican-frontmark
PLUGINS = [
 'frontmark', # Very useful for migrating from Jekyll
]
#
# See https://docs.getpelican.com/en/stable/content.html#articles-and-pages
FILENAME_METADATA = '(?P<title>.*)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_CATEGORY = ''
# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
