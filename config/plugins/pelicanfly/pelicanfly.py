import os
from pelican import signals
from fontawesome_markdown import FontAwesomeExtension

import logging
logger = logging.getLogger(__name__)


def add_md_ext_and_static(peli):
    md_ext = peli.settings.get('MARKDOWN')['extensions']
    cls = FontAwesomeExtension
    inst = cls()
    if not any([isinstance(ext, cls) for ext in md_ext]):
        md_ext.append(inst)
        peli.settings['MD_EXTENSIONS'] = md_ext
    pelifly_static = os.path.join(os.path.split(__file__)[0], 'static/fonts')
    # peli.settings['THEME_STATIC_PATHS'].append(pelifly_static)
    # for Assets plugin Bundling
    pelifly_css = os.path.join(os.path.split(__file__)[0], 'static/css')
    # peli.settings.setdefault('ASSET_SOURCE_PATHS', []).append(pelifly_css)


def publish_fontawesome_assets(peli):
    if peli.settings['PELICANFLY_PUBLISH_IN_CSS']:
        css_file = os.path.join(peli.output_path, 'themes', 'css', peli.settings['CSS_FILE'])
        with open(css_file, "r+") as f:
            s = f.read()
            f.seek(0)
            f.write("@import url('font-awesome.css');\n" + s)


def register():
    signals.initialized.connect(add_md_ext_and_static)
    signals.finalized.connect(publish_fontawesome_assets)
