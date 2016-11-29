[![Travis](https://img.shields.io/travis/patyk/streamshift.svg)](https://travis-ci.org/patyk/streamshift)
[![Coverage Status](https://coveralls.io/repos/github/patyk/streamshift/badge.svg?branch=master)](https://coveralls.io/github/patyk/streamshift?branch=master)
[![Github All Releases](https://img.shields.io/github/downloads/patyk/streamshift/total.svg)]()

# streamshift

## Synopsis

Listening to radio station originating in different timezone is odd - nighttime programme is not exactly what you'd expect in the morning. Enter streamshift - buffer audio streams, and serve them back with a user-defined offset.

## Running

### Config
```
[global]
buffer_dir = ./data/
port = 5000

[stream1]
url = http://stream3.polskieradio.pl:8904/
buffer = 86400 # number of seconds to buffer
```

### Buffer audio streams
```
streamshift buffer --config=./config.cfg
```

### Serve over http
```
streamshift web --config=./config.cfg
```

## Setup & hacking
```
virtualenv .
. ./bin/activate
pip install -r requirements.txt
nosetests --exe
```
