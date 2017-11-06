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

PATH             = '../content/linergaff'

PAGE_PATHS       = ['pages']
PAGE_EXCLUDES    = []
ARTICLE_PATHS    = ['posts']
ARTICLE_EXCLUDES = []
STATIC_PATHS     = ['linergaff', 'images']
STATIC_EXCLUDES  = ['linergaff/assets/.raw']





# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

ROOT_URL               = 'linergaff/'

INDEX_SAVE_AS          = ROOT_URL + 'blog/index.html'
ARTICLE_URL            = ROOT_URL + 'blog/a/{slug}'
ARTICLE_SAVE_AS        = ROOT_URL + 'blog/a/{slug}/index.html'
DRAFT_URL              = ROOT_URL + 'blog/drafts/{slug}.html'
DRAFT_SAVE_AS          = ROOT_URL + 'blog/drafts/{slug}.html'
PAGE_URL               = ROOT_URL + '{slug}/'
PAGE_SAVE_AS           = ROOT_URL + '{slug}/index.html'
CATEGORIES_URL         = ROOT_URL + 'blog/categories/'
CATEGORIES_SAVE_AS     = ROOT_URL + 'blog/categories/index.html'
CATEGORY_URL           = ROOT_URL + 'blog/categories/{slug}/'
CATEGORY_SAVE_AS       = ROOT_URL + 'blog/categories/{slug}/index.html'
ARCHIVES_URL           = ROOT_URL + 'blog/archives/'
ARCHIVES_SAVE_AS       = ROOT_URL + 'blog/archives/index.html'






# ████████ ███████ ███    ███ ██████  ██       █████  ████████ ███████
#    ██    ██      ████  ████ ██   ██ ██      ██   ██    ██    ██
#    ██    █████   ██ ████ ██ ██████  ██      ███████    ██    █████
#    ██    ██      ██  ██  ██ ██      ██      ██   ██    ██    ██
#    ██    ███████ ██      ██ ██      ███████ ██   ██    ██    ███████

# DIRECT_TEMPLATES = ['index', categories]
DIRECT_TEMPLATES           = ['index', 'archives', 'categories']
PAGINATED_DIRECT_TEMPLATES = ['index']
# TEMPLATE_PAGES             = {'gallery.html': 'gallery.html'}
EXTRA_TEMPLATES_PATHS      = ['theme/templates/linergaff'] # relative to pwd of scripts





# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_BASE_FOLDER      = ROOT_URL + 'blog/feed/'

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

PLUGINS = [
    'summary',
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.vimeo',
    'liquid_tags.soundcloud',
    'extract_toc',
    'pelican-linkclass',
    'pelicanfly',
    'assets',
    'gallery',
    'thumbnailer',
    'archives_per_category'
]


# [archives_per_category]
ARCHIVES_PER_CATEGORY_URL     = ROOT_URL + 'blog/archives/{category}/'
ARCHIVES_PER_CATEGORY_SAVE_AS = ROOT_URL + 'blog/archives/{category}/index.html'



# [assets]
css_linergaff = ['linergaff/main.css', 'linergaff/menu.css']

css_linergaff_page = css_content + ['fragments/forms.css', 'linergaff/main.css', 'linergaff/index.css', 'linergaff/donate.css', 'linergaff/request.css', 'linergaff/contact.css', 'linergaff/menu.css',
    'linergaff/guides.css']


asset_linergaff_base = ('css-linergaff-base',
                css_linergaff,
                {'output': 'css/liner-gaff-base.min.css', 'filters': 'yui_css'})

asset_linergaff_page = ('css-linergaff-page',
                css_linergaff_page,
                {'output': 'css/liner-gaff-page.min.css', 'filters': 'yui_css'})


ASSET_BUNDLES += [
    asset_linergaff_base,
    asset_linergaff_page
]




# [gallery]
GALLERY_PATH   = 'images'

# [thumbnailer]
IMAGE_PATH     = 'images'
