#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.path.dirname(__file__))
from blog_conf import *


# Thumbnailer will run
# NOTHING ELSE
#
# No Other Confs should deal with thumbs for blog


# ██████  ███████ ███████  █████  ██    ██ ██   ████████
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██   ██ █████   █████   ███████ ██    ██ ██      ██
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██████  ███████ ██      ██   ██  ██████  ███████ ██

# PATH             = '../content/blog'
OUTPUT_PATH      = "../.output"

PAGE_PATHS       = ['']
PAGE_EXCLUDES    = ['pages', 'posts']
ARTICLE_PATHS    = []
ARTICLE_EXCLUDES = ['posts', 'pages']
STATIC_PATHS     = []
STATIC_EXCLUDES  = ['images']





# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

INDEX_SAVE_AS      = False

ARTICLE_URL        = False
ARTICLE_SAVE_AS    = False

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

DIRECT_TEMPLATES = []





# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_ATOM             = None
FEED_RSS              = None




# ██████  ██      ██    ██  ██████  ██ ███    ██ ███████
# ██   ██ ██      ██    ██ ██       ██ ████   ██ ██
# ██████  ██      ██    ██ ██   ███ ██ ██ ██  ██ ███████
# ██      ██      ██    ██ ██    ██ ██ ██  ██ ██      ██
# ██      ███████  ██████   ██████  ██ ██   ████ ███████

# even though no pages are produced, they are required to get no errors due to templates

PLUGINS = [
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.soundcloud',
    'pelican-linkclass',
    'assets',
    'thumbnailer'
]
