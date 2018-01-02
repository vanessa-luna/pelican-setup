# -*- coding: utf-8 -*-

# Inject CDN into output.
#
# This is rather abstract and reall is simply a regex.sub plugin after the fact.
# The customizations should really be a tuple with a [pattern, repl] and just go.
# Based off this plugin which was too strict for my regex pattern
# https://github.com/fangpeishi/cdn_support
#
# Namely, in my code I have javascript which doesn't form complete urls but which still needed regexing.

import sys
import os
import re
from pelican import signals

reload(sys)
sys.setdefaultencoding('utf8')


def go (pelican):
    pattern = pelican.settings['CDN_REGEX']
    prefix = pelican.settings['CDN_PREFIX']

    for root, dirs, files in os.walk(pelican.settings['OUTPUT_PATH']):
        for outfile in files:
            if os.path.splitext(outfile)[1] in [".html", ".htm"]:
                file_path = os.path.join(root, outfile)
                with open(file_path, "r+") as f:
                    src = f.read()
                    # REGEXP

                    src = re.sub(pattern, prefix, src)
                    f.seek(0)
                    f.write(src)


def register():
    signals.finalized.connect(go)
