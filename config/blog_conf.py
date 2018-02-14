#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


#  TOC
#    default
#    theme
#    url
#    date & time
#    template
#    metadata
#    feed
#    paging
#    i18n
#    ordering
#
#    customizations
#    plugins



# ██████  ███████ ███████  █████  ██    ██ ██   ████████
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██   ██ █████   █████   ███████ ██    ██ ██      ██
# ██   ██ ██      ██      ██   ██ ██    ██ ██      ██
# ██████  ███████ ██      ██   ██  ██████  ███████ ██

SITENAME                   = u'Vanessa &#xe80a; Luna'
SITEURL                    = 'https://vanessa-luna.github.io'

PATH                       = '../content/blog'
OUTPUT_PATH                = '../.output/'
PAGE_PATHS                 = ['pages']
PAGE_EXCLUDES              = []
ARTICLE_PATHS              = ['posts']
ARTICLE_EXCLUDES           = []
STATIC_PATHS               = ['images']
STATIC_EXCLUDES            = []

WITH_FUTURE_DATES          = False
# SUMMARY_MAX_LENGTH         = 50
# DEFAULT_CATEGORY           = 'misc'

DISPLAY_PAGES_ON_MENU      = False
DISPLAY_CATEGORIES_ON_MENU = False
# DOCUTILS_SETTINGS          = {}

DELETE_OUTPUT_DIRECTORY    = False
# READERS                    = {}
# IGNORE_FILES               = ['.#*']
# JINJA_ENVIRONMENT          = {'trim_blocks': True, 'lstrip_blocks': True }
# JINJA_FILTERS              = {}
# JINJA_EXTENSIONS           = ['jinja2.ext.do']
# OUTPUT_SOURCES             = False
# OUTPUT_SOURCES_EXTENSION   = '.text'
# STATIC_EXCLUDE_SOURCES     = True
# TYPOGRIFY                  = False
# TYPOGRIFY_IGNORE_TAGS      = []
# INTRASITE_LINK_REGEX       = '[{|](?P<what>.*?)[|}]'
# PYGMENTS_RST_OPTIONS       = []
SLUGIFY_SOURCE             = 'basename'

CACHE_CONTENT              = True
CONTENT_CACHING_LAYER      = 'reader' # 'generator' #
CACHE_PATH                 = '.cache'
GZIP_CACHE                 = True
LOAD_CONTENT_CACHE         = True

# OUTPUT_RETENTION           = []
# LOG_FILTER                 = []
# CHECK_MODIFIED_METHOD      = 'mtime'
# WRITE_SELECTED             = []
# FORMATTED_FIELDS           = ['summary']



# ████████ ██   ██ ███████ ███    ███ ███████
#    ██    ██   ██ ██      ████  ████ ██
#    ██    ███████ █████   ██ ████ ██ █████
#    ██    ██   ██ ██      ██  ██  ██ ██
#    ██    ██   ██ ███████ ██      ██ ███████

THEME              = 'theme'
CSS_FILE           = 'base.css'
# THEME_STATIC_DIR   = 'static'
# THEME_STATIC_PATHS = ['static/dist']



# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
# ██    ██ ██████  ██
# ██    ██ ██   ██ ██
#  ██████  ██   ██ ███████

# RELATIVE_URLS = False
INDEX_SAVE_AS          = 'index.html'
ARTICLE_URL            = 'posts/{slug}.html'
ARTICLE_SAVE_AS        = 'posts/{slug}.html'
DRAFT_URL              = 'drafts/{slug}.html'
DRAFT_SAVE_AS          = 'drafts/{slug}.html'
PAGE_URL               = '{slug}/'
PAGE_SAVE_AS           = '{slug}/index.html'
CATEGORIES_URL         = 'categories/'
CATEGORIES_SAVE_AS     = 'categories/index.html'
CATEGORY_URL           = 'categories/{slug}/'
CATEGORY_SAVE_AS       = 'categories/{slug}/index.html'
ARCHIVES_URL           = 'archives/'
ARCHIVES_SAVE_AS       = 'archives/index.html'
TAGS_SAVE_AS           = False
AUTHOR_SAVE_AS         = False  # 'author/{slug}.html'
# TAG_URL                = 'tag/{slug}.html'
# AUTHOR_URL             = 'author/{slug}.html'
# YEAR_ARCHIVE_SAVE_AS   = ''
# MONTH_ARCHIVE_SAVE_AS  = ''
# DAY_ARCHIVE_SAVE_AS    = ''

ARTICLE_LANG_SAVE_AS   = False #'{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS     = False #'drafts/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS      = False #'pages/{slug}-{lang}.html'
# ARTICLE_LANG_URL       = '{slug}-{lang}.html'
# DRAFT_LANG_URL         = 'drafts/{slug}-{lang}.html'
# PAGE_LANG_URL          = 'pages/{slug}-{lang}.html'

# SLUG_SUBSTITUTIONS     = ( ('category/shadows', 'shadows'), )
# AUTHOR_SUBSTITUTIONS   = ()
# CATEGORY_SUBSTITUTIONS = ()
# TAG_SUBSTITUTIONS      = ()



# ██████   █████  ████████ ███████         ████████ ██ ███    ███ ███████
# ██   ██ ██   ██    ██    ██                 ██    ██ ████  ████ ██
# ██   ██ ███████    ██    █████              ██    ██ ██ ████ ██ █████
# ██   ██ ██   ██    ██    ██                 ██    ██ ██  ██  ██ ██
# ██████  ██   ██    ██    ███████            ██    ██ ██      ██ ███████

TIMEZONE            = 'America/New_York'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
# DEFAULT_DATE        = None
# DATE_FORMATS        = {}
# LOCALE              = ()



# ████████ ███████ ███    ███ ██████  ██       █████  ████████ ███████
#    ██    ██      ████  ████ ██   ██ ██      ██   ██    ██    ██
#    ██    █████   ██ ████ ██ ██████  ██      ███████    ██    █████
#    ██    ██      ██  ██  ██ ██      ██      ██   ██    ██    ██
#    ██    ███████ ██      ██ ██      ███████ ██   ██    ██    ███████

DIRECT_TEMPLATES           = ['index', 'archives', 'categories']
PAGINATED_DIRECT_TEMPLATES = ['index']
# TEMPLATE_PAGES             = {'gallery.html': 'gallery.html'}
# EXTRA_TEMPLATES_PATHS      = []



# ███    ███ ███████ ████████  █████  ██████   █████  ████████  █████
# ████  ████ ██         ██    ██   ██ ██   ██ ██   ██    ██    ██   ██
# ██ ████ ██ █████      ██    ███████ ██   ██ ███████    ██    ███████
# ██  ██  ██ ██         ██    ██   ██ ██   ██ ██   ██    ██    ██   ██
# ██      ██ ███████    ██    ██   ██ ██████  ██   ██    ██    ██   ██

AUTHOR              = u'Luna Umbra'
# DEFAULT_METADATA    = {}
# FILENAME_METADATA   = '(?P<date>d{4}-d{2}-d{2}).*'
# PATH_METADATA       = ''
# EXTRA_PATH_METADATA = {}



# ███████ ███████ ███████ ██████
# ██      ██      ██      ██   ██
# █████   █████   █████   ██   ██
# ██      ██      ██      ██   ██
# ██      ███████ ███████ ██████

FEED_BASE_FOLDER      = 'feed/'

# FEED_DOMAIN = None, i.e. base URL is "/"
FEED_MAX_ITEMS        = 13
RSS_FEED_SUMMARY_ONLY = False

FEED_ATOM             = None
FEED_RSS              = FEED_BASE_FOLDER + 'rss.xml'
CATEGORY_FEED_RSS     = FEED_BASE_FOLDER + '%s-rss.xml'
# FEED_ALL_RSS = FEED_BASE_FOLDER + 'rss-all.xml'

TAG_FEED_RSS          = None
AUTHOR_FEED_RSS       = None
TRANSLATION_FEED_RSS  = None

FEED_ALL_ATOM         = None
FEED_ALL_ATOM         = None
TAG_FEED_ATOM         = None
AUTHOR_FEED_ATOM      = None
CATEGORY_FEED_ATOM    = None # 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None



# ██████   █████   ██████  ██ ███    ██  ██████
# ██   ██ ██   ██ ██       ██ ████   ██ ██
# ██████  ███████ ██   ███ ██ ██ ██  ██ ██   ███
# ██      ██   ██ ██    ██ ██ ██  ██ ██ ██    ██
# ██      ██   ██  ██████  ██ ██   ████  ██████

DEFAULT_ORPHANS    = 0
DEFAULT_PAGINATION = 13
# PAGINATION_PATTERNS = (minimum page, URL setting, SAVE_AS setting)
PAGINATION_PATTERNS = (
    (1, '{base_name}/',          '{base_name}/index.html'         ),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)



# ██  ██  █████  ███    ██
# ██ ███ ██   ██ ████   ██
# ██  ██  █████  ██ ██  ██
# ██  ██ ██   ██ ██  ██ ██
# ██  ██  █████  ██   ████

DEFAULT_LANG          = u'en'
# TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
# TRANSLATION_FEED_RSS  = None, i.e. no RSS



#  ██████  ██████  ██████  ███████ ██████  ██ ███    ██  ██████
# ██    ██ ██   ██ ██   ██ ██      ██   ██ ██ ████   ██ ██
# ██    ██ ██████  ██   ██ █████   ██████  ██ ██ ██  ██ ██   ███
# ██    ██ ██   ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██    ██
#  ██████  ██   ██ ██████  ███████ ██   ██ ██ ██   ████  ██████

# NEWEST_FIRST_ARCHIVES  = True
# REVERSE_CATEGORY_ORDER = False
# ARTICLE_ORDER_BY       = 'reversed-date'
# PAGE_ORDER_BY          = 'basename'










# █████ █████ █████ █████ █████ █████ █████ █████ █████ █████











#  ██████ ██    ██ ███████ ████████  ██████  ███    ███ ██ ███████ ███████
# ██      ██    ██ ██         ██    ██    ██ ████  ████ ██    ███  ██
# ██      ██    ██ ███████    ██    ██    ██ ██ ████ ██ ██   ███   █████
# ██      ██    ██      ██    ██    ██    ██ ██  ██  ██ ██  ███    ██
#  ██████  ██████  ███████    ██     ██████  ██      ██ ██ ███████ ███████

PROFILE_IMAGE = 'favicon.png'
SUBTITLE = 'A reflection of your experience: as moonlight is a reflection of sunlight.'
# ( "text", ""|[] icons, "url")
SIDEBAR_LINKS = (
    ('Home',      ['flight', 'rocket', 'fighter-jet', 'space-shuttle'], '/'),
    ('Categories', ['leaf', 'feather', 'tree-2'], '/categories'),
    ('Archive',    ['hourglass-3', 'hourglass-2', 'hourglass-1'], '/archives/'),
    ('', '', ''),
    ('Gallery',    ['picture', 'eye-off', 'eye'], '/images'),
    ('', '', ''),
    ('About',      ['dot-circled', 'sun-1'], '/about'),
    ('Contact',    ['thumbs-up', 'hand-paper-o', 'hand-scissors-o', 'hand-grab-o'], '/contact')
    # ('', '', ''),
    # ('Liner Gaff', ['transgender-alt'], '/liner-gaff')
)
SIDEBAR_SECRET = "/s"

# random bg code
# builds {SITEURL}/{IMAGE_PATH | THUMBNAIL_DIR/THUMBNAIL_SIZE}/
#        {BG_GALLERY_NAME}/{random(BG_NUM_IMAGES)}{BG_IMAGE_SUFFIX}
BG_GALLERY_NAME = 'backgrounds'
BG_NUM_IMAGES = 25 # index chosen acts as prefix
BG_IMAGE_SUFFIX = 'cover.jpg'

COMMENTS_PAGE = "vanessa-luna"
GOOGLE_ANALYTICS = 'UA-100867520-1'
GAFF_ANALYTICS = "UA-108064387-1"


# ██████  ██      ██    ██  ██████  ██ ███    ██ ███████
# ██   ██ ██      ██    ██ ██       ██ ████   ██ ██
# ██████  ██      ██    ██ ██   ███ ██ ██ ██  ██ ███████
# ██      ██      ██    ██ ██    ██ ██ ██  ██ ██      ██
# ██      ███████  ██████   ██████  ██ ██   ████ ███████

PLUGIN_PATHS = ['plugins']
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
    'inject_cdn'                # replace img urls with cdn domain
]


MARKDOWN = {
    'extension_configs': {
        'toc': {}, # [extract_toc]
        'markdown.extensions.tables':{},
        'markdown.extensions.codehilite': {'css_class': 'highlight',
                                            'guess_lang': False},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# [pelican-linkclass]
LINKCLASS_INTERNAL_CLASS = 'internal'
LINKCLASS_EXTERNAL_CLASS = 'external'

# [pelicanfly]
PELICANFLY_PUBLISH_IN_CSS = False # prevents font-awesome.css injection




# [assets]
ASSET_SOURCE_PATHS = ['src/css', 'helpers']

# if only showing sidebar and nothing in the content...
css_base = ['base.css', 'fragments/sidebar.css', 'fragments/footer.css', 'page.css']
# if rendering a 'post' you need all this
css_content = css_base + ['fragments/content.css', 'fragments/syntax.css', 'fragments/forms.css']
css_paginated = ['fragments/pagination.css']
css_comments = ['fragments/comments.css']





css_gallery = ['fragments/gallery.css']
# js_gallery = ['jquery/jquery.min.js', 'fotorama/fotorama.js']

css_photoswipe = ['photoswipe/photoswipe.css', 'photoswipe/default-skin/default-skin.css']
js_photoswipe = ['photoswipe/photoswipe.min.js']
js_photoswipe_ui = ['photoswipe/photoswipe-ui-default.js']

js_validate = ['validator_js/validate.min.js']


# FRAGMENTS
asset_base = ('css-base', css_base,
            { 'output': 'css/base.min.css', 'filters': 'yui_css' })
asset_fragment_gallery = ('css-fragment-gallery', css_gallery,
            {'output': 'css/fragments/gallery-fragment.min.css', 'filters': 'yui_css'})
asset_fragment_photoswipe = ('css-fragment-photoswipe', css_photoswipe,
            {'output': 'css/fragments/photoswipe.min.css', 'filters': 'yui_css'})
asset_fragment_photoswipe_js = ('js-photoswipe', js_photoswipe,
                {'output':'js/photoswipe.js'})
asset_fragment_photoswipe_js_ui = ('js-photoswipe-ui', js_photoswipe_ui,
                {'output':'js/photoswipe_ui.js'})
asset_fragment_validate_js = ('js-validate', js_validate,
                {'output':'js/validate.js'})


# TEMPLATES
asset_index = ('css-index',
                css_content + css_paginated + ['index.css'],
                {'output': 'css/index.min.css', 'filters': 'yui_css'})
asset_article = ('css-article',
                css_content + css_paginated + css_comments + ['article.css'],
                {'output': 'css/article.min.css', 'filters': 'yui_css'})
asset_categories = ('css-categories',
                css_base + ['categories.css'],
                {'output': 'css/categories.min.css', 'filters': 'yui_css'})
asset_category = ('css-category',
                css_content + css_paginated + ['index.css'],
                {'output': 'css/category.min.css', 'filters': 'yui_css'})
asset_archives = ('css-archives',
                    css_base + ['archives.css'],
                    {'output': 'css/archives.min.css', 'filters': 'yui_css'})


# PAGES
asset_page = ('css-page',
                css_content,
                {'output': 'css/page.min.css', 'filters': 'yui_css'})
asset_page_gallery = ('css-gallery',
            css_base + css_gallery + ['gallery.css'],
            {'output': 'css/gallery.min.css', 'filters': 'yui_css'})
asset_article_gallery = ('css-article-gallery',
            ['gallery.css'],
            {'output': 'css/gallery-article.min.css', 'filters': 'yui_css'})




ASSET_BUNDLES = [
    asset_base,
    asset_fragment_gallery,
    asset_index,
    asset_article,
    asset_categories,
    asset_category,
    asset_archives,
    asset_page,
    asset_page_gallery,
    asset_article_gallery,
    asset_fragment_photoswipe,
    asset_fragment_photoswipe_js,
    asset_fragment_photoswipe_js_ui,
    asset_fragment_validate_js
]



# [gallery]
GALLERY_PATH ='images'

# [thumbnailer]
# note: will not make images any bigger despite options
IMAGE_PATH = 'images' # path to folder of images to process
THUMBNAIL_DIR = 'thumb' # where to place resizes
THUMBNAIL_SIZES = {
    'tiny'   : '?x144',
    'smaller': '?x240',
    'small'  : '?x360',
    'medium' : '?x480',
    'large'  : '?x720',
    'huge'   : '?x1080'
}# The generated filename will be originalname_thumbnailname.ext unless THUMBNAIL_KEEP_NAME is set.
THUMBNAIL_KEEP_NAME = True # is a Boolean that, if set, puts the file with the original name in a thumbnailname folder, named like the key in THUMBNAIL_SIZES.
THUMBNAIL_KEEP_TREE = True # is a Boolean that, if set, saves the image directory tree.

# [summary]
SUMMARY_BEGIN_MARKER = "[summary begin]"
SUMMARY_END_MARKER = "[summary end]"
SUMMARY_USE_FIRST_PARAGRAPH = False;
SUMMARY_REMOVE_META = "removeSummary"

# [archives_per_category]
ARCHIVES_PER_CATEGORY_URL           = 'archives/{category}/'
ARCHIVES_PER_CATEGORY_SAVE_AS       = 'archives/{category}/index.html'
# CATEGORIES_TO_ARCHIVE               =
# DAY_ARCHIVES_PER_CATEGORY_SAVE_AS   =
# MONTH_ARCHIVES_PER_CATEGORY_SAVE_AS =
# YEAR_ARCHIVES_PER_CATEGORY_SAVE_AS  = 'archives/{category}/{date}.html'


#[inject_cdn]
CDN_PREFIX = "https://res.cloudinary.com/vanessa-luna/image/upload"
# capture github domain if exists,
# if not, then if before the url is a
# src, url or href
CDN_REGEX = '(https://vanessa-luna\.github\.io|' \
            '(?<=src\=")|' \
            '(?<=url\()|' \
            "(?<=url\(')|" \
            '(?<=href\=))' \
            '(?=/thumb/|/images/)'
