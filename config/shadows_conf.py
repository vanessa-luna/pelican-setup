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

PAGE_PATHS = ['']
PAGE_EXCLUDES = ['pages', 'posts', 'liner-gaff', 'images']
ARTICLE_PATHS = ['shadows']
ARTICLE_EXCLUDES = ['posts']
STATIC_PATHS = []
STATIC_EXCLUDES = ['images', 'liner-gaff']





# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

INDEX_SAVE_AS      = 's/posts/index.html'

ARTICLE_URL        = 's/posts/{slug}.html'
ARTICLE_SAVE_AS    = 's/posts/{slug}.html'

TAGS_SAVE_AS       = False
ARCHIVES_SAVE_AS   = False
CATEGORY_SAVE_AS   = False
CATEGORIES_SAVE_AS = False





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

DIRECT_TEMPLATES = ['index']





# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_ATOM             = None
FEED_RSS              = None
# FEED_ALL_RSS          = None
# CATEGORY_FEED_RSS     = None

# TAG_FEED_RSS          = None
# AUTHOR_FEED_RSS       = None
# TRANSLATION_FEED_RSS  = None

# FEED_ALL_ATOM         = None
# FEED_ALL_ATOM         = None
# TAG_FEED_ATOM         = None
# AUTHOR_FEED_ATOM      = None
# CATEGORY_FEED_ATOM    = None
# TRANSLATION_FEED_ATOM = None





# ██████  ██      ██    ██  ██████  ██ ███    ██ ███████
# ██   ██ ██      ██    ██ ██       ██ ████   ██ ██
# ██████  ██      ██    ██ ██   ███ ██ ██ ██  ██ ███████
# ██      ██      ██    ██ ██    ██ ██ ██  ██ ██      ██
# ██      ███████  ██████   ██████  ██ ██   ████ ███████


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
    'date_utils'
]
