#!/usr/bin/env python
# from loadfile import RadioUploader
# from deletefile import RadioCleaner

from flask import Flask
from flask import Response
from streamshift.stream import Stream, ChunkManager

import ConfigParser


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/station/')
def index():
    # station index
    return ''

@app.route('/station/<string:name>/<int:shift_offset>')
def station(name, shift_offset):
    url = app.config["URLS"][name]
    stream = Stream(# TODO
        url=url,
        cm=ChunkManager('./data/', url, shift_offset)
    ).listen()

    return Response(stream, mimetype='audio/mpeg')
