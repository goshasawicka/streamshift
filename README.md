[![Travis](https://img.shields.io/travis/patyk/streamshift.svg)](https://travis-ci.org/patyk/streamshift)
[![Coverage Status](https://coveralls.io/repos/github/patyk/streamshift/badge.svg?branch=master)](https://coveralls.io/github/patyk/streamshift?branch=master)
[![Github All Releases](https://img.shields.io/github/downloads/patyk/streamshift/total.svg)]()

# streamshift

## Synopsis

Listening to favorite radio station from a different timezone gets weird - nighttime programme is not exactly what you'd want in the morning. Enter streamshift - it buffers audio streams, and serves them back with a user-defined offset.

## Running

### Config
```
[global]
buffer_dir = ./data/

[stream1]
url = http://stream3.polskieradio.pl:8904/
buffer = 86400 # how many much history to keep locally
```

### Buffering
```
./manage.py
```

### Serving
```
./main.py
```
Flask app will listen on port 5000 by default

## Setup & hacking
```
virtualenv .
. ./bin/activate
pip install -r requirements.txt
nosetests --exe
```
