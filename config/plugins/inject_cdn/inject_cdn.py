# -*- coding: utf-8 -*-

import sys
import os
import re
from pelican import signals


def go (pelican):
    for root, dirs, files in os.walk(pelican.settings['OUTPUT_PATH']):
        for outfile in files:
            if os.path.splitext(outfile)[1] in [".html", ".htm"]:
                file_path = os.path.join(root, outfile)
                with open(file_path, "r+") as f:
                    src = f.read()
                    # REGEXP
                    pattern = '(https://vanessa-luna\.github\.io|(?<=src\=")|(?<=url\())(?=/thumb/|/images/)'
                    prefix = "http://res.cloudinary.com/vanessa-luna/image/upload"
                    src = re.sub(pattern, prefix, src)
                    f.seek(0)
                    f.write(src)


def register():
    signals.finalized.connect(go)
