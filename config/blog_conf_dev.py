
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.path.dirname(__file__))
from blog_conf import *


OUTPUT_PATH        = '../.dev-output/'
SITEURL            = ''

CACHE_CONTENT      = False
LOAD_CONTENT_CACHE = False

GOOGLE_ANALYTICS   = ''
GAFF_ANALYTICS     = ''



PLUGINS = [
    'summary',                  # specify summary in content
    'liquid_tags.img',          # allows {% img %} in content
    'liquid_tags.youtube',      # allows {% youtube %} in content
    'liquid_tags.vimeo',        # allows {% youtube %} in content
    'liquid_tags.soundcloud',   # allows {% soundcloud %} in content
    'extract_toc',              # can render table of contents from post
    'pelican-linkclass',        # indicator for links leaving domain
    'pelicanfly',               # adds font awesome support
    'assets',                   # adds compiler for assets
    'gallery',                  # adds gallery support to content
    'archives_per_category',    # generates archive page per category
    'category_meta'
]
