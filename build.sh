#!/usr/bin/env bash

PY=${PY:-python}
PELICAN=${PELICAN:-pelican}

BASEDIR=$(pwd)
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/.output

CONFDIR=$BASEDIR/config

BLOG_CONF=$CONFDIR/blog_conf.py
LINERGAFF_CONF=$CONFDIR/linergaff_conf.py
SHADOWS_CONF=$CONFDIR/shadows_conf.py
THUMBS_CONF=$CONFDIR/thumbnail_conf.py


# Build both confs
$PELICAN -s $THUMBS_CONF    -o $OUTPUTDIR $INPUTDIR
$PELICAN -s $LINERGAFF_CONF -o $OUTPUTDIR $INPUTDIR
$PELICAN -s $SHADOWS_CONF   -o $OUTPUTDIR $INPUTDIR
$PELICAN -s $BLOG_CONF      -o $OUTPUTDIR $INPUTDIR



# IF SEND IN OPTION DON'T GIT THAT SHIT...
if [[ ($# -eq 0) ]]; then
    # git
    cd .output
    git add .
    git commit -m "update"
    git push
fi
