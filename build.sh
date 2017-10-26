#!/usr/bin/env bash

PY=${PY:-python}
PELICAN=${PELICAN:-pelican}

BASE_DIR=$(pwd)

OUTPUTDIR=$BASE_DIR/.output

CONTENT_DIR=$BASE_DIR/content
BLOG_INPUT_DIR=$CONTENT_DIR/blog
LINERGAFF_INPUT_DIR=$CONTENT_DIR/liner-gaff
SHADOWS_INPUT_DIR=$CONTENT_DIR/shadows

CONFDIR=$BASE_DIR/config
BLOG_CONF=$CONFDIR/blog_conf.py
LINERGAFF_CONF=$CONFDIR/linergaff_conf.py
SHADOWS_CONF=$CONFDIR/shadows_conf.py
THUMBS_CONF=$CONFDIR/thumbnail_conf.py


# Build both confs
$PELICAN -s $THUMBS_CONF    -o $OUTPUTDIR $BLOG_INPUT_DIR
$PELICAN -s $LINERGAFF_CONF -o $OUTPUTDIR $LINERGAFF_INPUT_DIR
$PELICAN -s $SHADOWS_CONF   -o $OUTPUTDIR $SHADOWS_INPUT_DIR
$PELICAN -s $BLOG_CONF      -o $OUTPUTDIR $BLOG_INPUT_DIR



# IF SEND IN OPTION DON'T GIT THAT SHIT...
if [[ ($# -eq 0) ]]; then
    # git
    cd $OUTPUTDIR
    git commit -a -m "update"
    git push

    cd $BASEDIR
    git commit -a -m "update"
    git push

    cd $INPUTDIR
    git commit -a -m "update"
    git push
fi
