#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Zachery Bir'
SITENAME = u'Zac Bir'
SITESUBTITLE = u'Thinking and occasionally typing as a service'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'misc'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Menu items
MENUITEMS = (('Code', 'http://github.com/zacbir/'),
             ('Twitter', 'http://twitter.com/zacbir/'),
             ('Archives', '/archives.html'))

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

CATEGORIES = ()

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# AUTHOR_SAVE_AS = False
# AUTHORS_SAVE_AS = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'pelican-octopress-theme'

PLUGIN_PATHS = ['/Users/zac.bir/Development/zacbir.net/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.include_code', 'tipue_search']

DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['code', 'images', 'static', '.well-known']

CUSTOM_CSS_FILE = 'static/css/custom.css'
