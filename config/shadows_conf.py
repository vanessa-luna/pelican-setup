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

PATH             = 'content/shadows'

PAGE_PATHS       = ['pages']
PAGE_EXCLUDES    = []
ARTICLE_PATHS    = ['shadows']
ARTICLE_EXCLUDES = []
STATIC_PATHS     = []
STATIC_EXCLUDES  = []




# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

INDEX_SAVE_AS      = 's/posts/index.html'

ARTICLE_URL        = 's/posts/{slug}.html'
ARTICLE_SAVE_AS    = 's/posts/{slug}.html'

ARCHIVES_URL       = 's/archives/'
ARCHIVES_SAVE_AS   = 's/archives/index.html'

PAGE_URL           = 's/{slug}/'
PAGE_SAVE_AS       = 's/{slug}/index.html'

TAGS_SAVE_AS       = False
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

DIRECT_TEMPLATES        = ['index', 'archives']
EXTRA_TEMPLATES_PATHS   = ['theme/templates/shadows'] # relative to pwd of scripts




# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_ATOM             = None
FEED_RSS              = None



#  ██████ ██    ██ ███████ ████████  ██████  ███    ███ ██ ███████ ███████
# ██      ██    ██ ██         ██    ██    ██ ████  ████ ██    ███  ██
# ██      ██    ██ ███████    ██    ██    ██ ██ ████ ██ ██   ███   █████
# ██      ██    ██      ██    ██    ██    ██ ██  ██  ██ ██  ███    ██
#  ██████  ██████  ███████    ██     ██████  ██      ██ ██ ███████ ███████

SITENAME = " Inanis &#xe80a; Umbra"
SUBTITLE = 'Within the shadows lies the honesty we seek yet fear the most. Oversharing &#xe813;'
SIDEBAR_LINKS = (
    ('Shadows',   ['cloud-moon-inv', 'moon'],       '/s/posts'),
    ('Archive',   ['hourglass-o', 'hourglass'],     '/s/archives/'),
    ('', '', ''),
    ('About',     ['dot-circled', 'cloud-sun-inv'], '/s/about'),
    # ('Gallery',    ['picture', 'eye-off', 'eye'], '/images'),
    # ('', '', ''),
    # ('Contact',    ['thumbs-up', 'hand-paper-o', 'hand-scissors-o', 'hand-grab-o'], '/contact')
    # ('', '', ''),
    # ('Liner Gaff', ['transgender-alt'], '/liner-gaff')
)






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



css_shadows = ['shadows/base.css']

# LINER-GAFF
asset_shadows_base = ('css-shadows-base',
                css_shadows,
                {'output': 'css/shadows.min.css', 'filters': 'yui_css'})


ASSET_BUNDLES += [asset_shadows_base]
