#!/usr/bin/env bash

PY=${PY:-python}
PELICAN=${PELICAN:-pelican}

# important folders
BASE_DIR=$(pwd)
CONF_DIR=$BASE_DIR/config
CONTENT_DIR=$BASE_DIR/content
PROD_OUTPUT_DIR=$BASE_DIR/.output
DEV_OUTPUT_DIR=$BASE_DIR/.dev-output

# config locations
THUMBS_CONF=$CONF_DIR/thumbnail_conf.py
LINERGAFF_CONF=$CONF_DIR/linergaff_conf_dev.py
SHADOWS_CONF=$CONF_DIR/shadows_conf_dev.py
BLOG_CONF=$CONF_DIR/blog_conf_dev.py

# PID management of running processes
PID_DIR=$BASE_DIR/.cache
SRV_PID=$PID_DIR/srv.pid
BLOG_PID=$PID_DIR/blog.pid
LINERGAFF_PID=$PID_DIR/linergaff.pid
SHADOWS_PID=$PID_DIR/shadows.pid
THUMBS_PID=$PID_DIR/thumbs.pid




function usage(){
    echo "usage: $0"
    echo "-h --help shows usage"
    echo "a = build all"
    echo "b = content"
    echo "l = liner-gaff"
    echo "s = shadows"
    echo "m = media"
    echo "no input will serve only"
    echo "any other input will stop (sdlfk)"
    echo ""
    exit 3
}




# ███████ ██   ██ ██    ██ ████████ ██████   ██████  ██     ██ ███    ██
# ██      ██   ██ ██    ██    ██    ██   ██ ██    ██ ██     ██ ████   ██
# ███████ ███████ ██    ██    ██    ██   ██ ██    ██ ██  █  ██ ██ ██  ██
#      ██ ██   ██ ██    ██    ██    ██   ██ ██    ██ ██ ███ ██ ██  ██ ██
# ███████ ██   ██  ██████     ██    ██████   ██████   ███ ███  ██   ████
#
# load up each .pid file and shut them down

function shut_down(){
  kill_pid $SRV_PID
  kill_pid $BLOG_PID
  kill_pid $LINERGAFF_PID
  kill_pid $SHADOWS_PID
  kill_pid $THUMBS_PID
}

function kill_pid {
    pid=$(cat $1)
    if [[ $? -eq 0 ]]; then
      if alive $pid; then
        echo "Stopping " $1
        kill $pid
      else
        echo "Stale PID, deleting" $1
      fi
      rm $1
    else
      echo $1 " file not found"
    fi
}
function alive() {
  kill -0 $1 >/dev/null 2>&1
}



# ███████ ████████  █████  ██████  ████████ ██    ██ ██████
# ██         ██    ██   ██ ██   ██    ██    ██    ██ ██   ██
# ███████    ██    ███████ ██████     ██    ██    ██ ██████
#      ██    ██    ██   ██ ██   ██    ██    ██    ██ ██
# ███████    ██    ██   ██ ██   ██    ██     ██████  ██
#
# run pelican for each conf file
# start python server
# make sure it all started up

function start_up(){
  echo "Starting up Pelican and HTTP server"
  shift
  media
  shadows
  linergaff
  content
  serve
  # ensure stuff started
  did_start $blog_pid
  did_start $linergaff_pid
  did_start $shadows_pid
  did_start $thumbs_pid
  did_start $srv_pid

}
function media() {
    ln -fsr .output/images .dev-output/
    # ln -fsr .output/images content/
    ln -fsr .output/thumb .dev-output/

    kill_pid $THUMBS_PID
    $PELICAN --autoreload -r $CONTENT_DIR -o $PROD_OUTPUT_DIR -s $THUMBS_CONF &
    thumbs_pid=$!
    echo $thumbs_pid > $THUMBS_PID
}
function shadows() {
    kill_pid $SHADOWS_PID
    $PELICAN --debug --autoreload -r $CONTENT_DIR -o $DEV_OUTPUT_DIR -s $SHADOWS_CONF &
    shadows_pid=$!
    echo $shadows_pid > $SHADOWS_PID
}
function linergaff() {
    kill_pid $LINERGAFF_PID
    $PELICAN --debug --autoreload -r $CONTENT_DIR -o $DEV_OUTPUT_DIR -s $LINERGAFF_CONF &
    linergaff_pid=$!
    echo $linergaff_pid > $LINERGAFF_PID
}

function content() {
    kill_pid $BLOG_PID
    $PELICAN --debug --autoreload -r $CONTENT_DIR -o $DEV_OUTPUT_DIR -s $BLOG_CONF &
    blog_pid=$!
    echo $blog_pid > $BLOG_PID
}

function serve () {
    kill_pid $SRV_PID
    # move to output dir and start server
    mkdir -p $DEV_OUTPUT_DIR && cd $DEV_OUTPUT_DIR
    $PY -m pelican.server $port &
    srv_pid=$!
    echo $srv_pid > $SRV_PID
}


function did_start() {
    sleep 1
    if ! alive $1 ; then
        echo "something didn't start"
        return 1
    fi
}




# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████

if [[ ($# -gt 1) || $1 == '-h' || $1 == '--help' ]]; then
    # HELP
    usage
elif [[ $# -eq 1 ]]; then
    #  SHUTDOWN
    shut_down

    if [[ $1 == 'a' ]]; then
        # RUN ALL
        start_up
    elif [[ $1 == 'b' ]]; then
        # BLOG
        content
        serve
        did_start $blog_pid
        did_start $srv_pid
    elif [[ $1 == 'l' ]]; then
        # LINERGAFF
        linergaff
        serve
        did_start $linergaff_pid
        did_start $srv_pid
    elif [[ $1 == 's' ]]; then
        # SHADOWS
        shadows
        serve
        did_start $shadows_pid
        did_start $srv_pid
    elif [[ $1 == 'm' ]]; then
        # MEDIA RUN
        media
        did_start $thumbs_pid
        kill $THUMBS_PID
    fi
else
  shut_down
  serve
  did_start $srv_pid
fi
