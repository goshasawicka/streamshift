import hashlib
import os
import urllib2
import time
import logging
from util import GenericObject



class Chunk(GenericObject):
    filepath = ""
    timestamp = ""
    buffer = ""

    def __init__(self, timestamp, path, cm):
        self.timestamp = timestamp
        self.filepath = path + str(timestamp)
        self.cm = cm

    def write(self, payload):
        self.logger.debug('Writing chunk %s' % str(self.timestamp))
        with open(self.filepath, "wb") as f:
            f.write(payload)

    def read(self):
        self.logger.debug('Reading chunk %s' % str(self.timestamp))
        with open(self.filepath, "rb") as f:
            return f.read()

    def delete(self):
        try:
            self.logger.debug('Deleting chunk %s' % str(self.timestamp))
            os.remove(self.filepath)
        except Exception as e:
            self.logger.critical("Can't find and remove chunk %s" % self.filepath)
            self.logger.critical(e)

    @property
    def seconds(self):
        try:
            return float(self.cm.next(self).timestamp) - float(self.timestamp)
        except AttributeError:
            print "Cannot find next file"

class ChunkManager(GenericObject):

    def __init__(self, path, url, shift):
        # self.buffer = buffer
        self.shift = shift

        # TODO: validation buffer > shift

        self.path = path + hashlib.md5(url).hexdigest() + "/"
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def find(self):
        self.logger.debug("Find chunk with offset %s" % str(self.shift))
        t = time.time() - self.shift
        files = sorted(os.listdir(self.path))

        for file in files:
            if t < float(file):
                self.logger.debug("Found %s" % file)
                return Chunk(file, self.path, self)

    def list(self):
        chunks = []
        for filename in sorted(os.listdir(self.path)):
            chunks.append(Chunk(filename, self.path, self))
        return chunks

    def next(self, chunk):
        list = self.list()
        try:
            for idx, file in enumerate(list):
                if file.timestamp == chunk.timestamp:
                    return list[idx + 1]
            return None
        except:
            return None

    def write(self, timestamp, payload):
        Chunk(timestamp=time.time(), path=self.path, cm=self).write(payload=payload)

class Stream(GenericObject):

    def __init__(self, url, cm):
        self.url = url
        self.cm = cm


    def listen(self):
        chunk = self.cm.find()
        while chunk:
            self.logger.info("Listening to chunk %d" % float(chunk.timestamp))
            yield chunk.read()
            self.logger.info("Waiting %d" % chunk.seconds)
            time.sleep(chunk.seconds)
            chunk = self.cm.next(chunk)

        self.logger.error("Run out of chunks")