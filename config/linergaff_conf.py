#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.path.dirname(__file__))
from blog_conf import *





# ██████  ███████ ███████  █████  ██    ██ ██   ████████
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██   ██ █████   █████   ███████ ██    ██ ██      ██
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██████  ███████ ██      ██   ██  ██████  ███████ ██

PAGE_PATHS = ['liner-gaff']
PAGE_EXCLUDES = ['pages', 'posts', 'images']
ARTICLE_PATHS = ['liner-gaff/posts']
ARTICLE_EXCLUDES = ['posts']
STATIC_PATHS = ['liner-gaff/assets']
STATIC_EXCLUDES = ['images', 'liner-gaff', 'liner-gaff/assets/.raw']





# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

INDEX_SAVE_AS          = 'liner-gaff/blog/index.html'
ARTICLE_URL            = 'liner-gaff/blog/a/{slug}'
ARTICLE_SAVE_AS        = 'liner-gaff/blog/a/{slug}/index.html'
DRAFT_URL              = 'liner-gaff/blog/drafts/{slug}.html'
DRAFT_SAVE_AS          = 'liner-gaff/blog/drafts/{slug}.html'
PAGE_URL               = 'liner-gaff/{slug}/'
PAGE_SAVE_AS           = 'liner-gaff/{slug}/index.html'
CATEGORIES_URL         = 'liner-gaff/blog/categories/'
CATEGORIES_SAVE_AS     = 'liner-gaff/blog/categories/index.html'
CATEGORY_URL           = 'liner-gaff/blog/categories/{slug}/'
CATEGORY_SAVE_AS       = 'liner-gaff/blog/categories/{slug}/index.html'
ARCHIVES_URL           = 'liner-gaff/blog/archives/'
ARCHIVES_SAVE_AS       = 'liner-gaff/blog/archives/index.html'






# ████████ ██   ██ ███████ ███    ███ ███████
#    ██    ██   ██ ██      ████  ████ ██
#    ██    ███████ █████   ██ ████ ██ █████
#    ██    ██   ██ ██      ██  ██  ██ ██
#    ██    ██   ██ ███████ ██      ██ ███████

THEME_STATIC_PATHS = []





# ████████ ███████ ███    ███ ██████  ██       █████  ████████ ███████
#    ██    ██      ████  ████ ██   ██ ██      ██   ██    ██    ██
#    ██    █████   ██ ████ ██ ██████  ██      ███████    ██    █████
#    ██    ██      ██  ██  ██ ██      ██      ██   ██    ██    ██
#    ██    ███████ ██      ██ ██      ███████ ██   ██    ██    ███████

# DIRECT_TEMPLATES = ['index', categories]
DIRECT_TEMPLATES           = ['index', 'archives', 'categories']
PAGINATED_DIRECT_TEMPLATES = ['index']
# TEMPLATE_PAGES             = {'gallery.html': 'gallery.html'}
EXTRA_TEMPLATES_PATHS      = ['theme/templates/liner-gaff'] # relative to pwd of scripts





# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_BASE_FOLDER      = 'liner-gaff/blog/feed/'

# FEED_DOMAIN = None, i.e. base URL is "/"
FEED_MAX_ITEMS        = 13
RSS_FEED_SUMMARY_ONLY = False

FEED_ATOM             = None
FEED_RSS              = FEED_BASE_FOLDER + 'rss.xml'
CATEGORY_FEED_RSS     = FEED_BASE_FOLDER + '%s-rss.xml'






# ██████   █████   ██████  ██ ███    ██  ██████
# ██   ██ ██   ██ ██       ██ ████   ██ ██
# ██████  ███████ ██   ███ ██ ██ ██  ██ ██   ███
# ██      ██   ██ ██    ██ ██ ██  ██ ██ ██    ██
# ██      ██   ██  ██████  ██ ██   ████  ██████

DEFAULT_PAGINATION = 5






#  ██████ ██    ██ ███████ ████████  ██████  ███    ███ ██ ███████ ███████
# ██      ██    ██ ██         ██    ██    ██ ████  ████ ██    ███  ██
# ██      ██    ██ ███████    ██    ██    ██ ██ ████ ██ ██   ███   █████
# ██      ██    ██      ██    ██    ██    ██ ██  ██  ██ ██  ███    ██
#  ██████  ██████  ███████    ██     ██████  ██      ██ ██ ███████ ███████



COMMENTS_PAGE = "liner-gaff"

# ██████  ██      ██    ██  ██████  ██ ███    ██ ███████
# ██   ██ ██      ██    ██ ██       ██ ████   ██ ██
# ██████  ██      ██    ██ ██   ███ ██ ██ ██  ██ ███████
# ██      ██      ██    ██ ██    ██ ██ ██  ██ ██      ██
# ██      ███████  ██████   ██████  ██ ██   ████ ███████

 # turn off thumbnailer basically...?
PLUGINS = [
    'summary',
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.soundcloud',
    'extract_toc',
    'pelican-linkclass',
    'pelicanfly',
    'assets',
    'gallery',
    'thumbnailer',
    'archives_per_category',
    'date_utils'
]


# [archives_per_category]
ARCHIVES_PER_CATEGORY_URL           = 'liner-gaff/blog/archives/{category}/'
ARCHIVES_PER_CATEGORY_SAVE_AS       = 'liner-gaff/blog/archives/{category}/index.html'


# [assets]
css_linergaff = ['liner-gaff/main.css', 'liner-gaff/menu.css']


asset_linergaff_blog = ('css-linergaff-blog',
                css_content + css_paginated + ['index.css'] + css_linergaff,
                {'output': 'css/liner-gaff-index.min.css', 'filters': 'yui_css'})

asset_linergaff_base = ('css-linergaff-base',
                css_linergaff,
                {'output': 'css/liner-gaff-base.min.css', 'filters': 'yui_css'})


ASSET_BUNDLES += [asset_linergaff_blog, asset_linergaff_base]




# [gallery]
GALLERY_PATH ='liner-gaff/images'

# [thumbnailer]
IMAGE_PATH = 'liner-gaff/images'
