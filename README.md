[![Travis](https://img.shields.io/travis/patyk/streamshift.svg)](https://travis-ci.org/patyk/streamshift)
[![Coverage Status](https://coveralls.io/repos/github/patyk/streamshift/badge.svg?branch=master)](https://coveralls.io/github/patyk/streamshift?branch=master)
[![Github All Releases](https://img.shields.io/github/downloads/patyk/streamshift/total.svg)]()
[![PyPI](https://img.shields.io/pypi/v/streamshift.svg)](https://pypi.python.org/pypi/streamshift)

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
### Command line:
### Buffer audio streams
```
streamshift_cli --mode buffer

```

### Serve over http
```
streamshift_cli --mode web
```

### Help
```
streamshift_cli --help
```
### Listening (on vlc)
```
vlc http://localhost:<port>/station/<station_name>/<offset_in_sec>
```

## Setup & hacking
```
virtualenv .
. ./bin/activate
pip install -r requirements.txt
nosetests --exe
(...)
python setup.py sdist upload -r pypi
```
