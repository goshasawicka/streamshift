import urllib2

import os
import time

from streamshift.util import GenericObject
from streamshift.stream import Stream, ChunkManager

BUFFER_SIZE = 1024 * 50


class StreamProcess(GenericObject):

    def __init__(self, config):
        self.url = config[0][1]
        self.buffer = config[1][1]
        self.shift = 10  # TODO should it stay or should it go?
        self.path = config[3][1]

        self.logger.info("New process %d" % os.getpid())
        self.cm = ChunkManager(self.path, self.url, self.shift)

    def purge(self):
        self.logger.info("Purging")
        while True:
            time.sleep(1)
            for chunk in self.cm.list():
                if float(time.time() - float(os.path.basename(chunk.timestamp))) > float(self.buffer):
                    self.logger.debug("Purge chunk %s" % os.path.basename(chunk.timestamp))
                    chunk.delete()


    def buffering(self):
        self.logger.info("Buffering")
        # stream = Stream(self.url, self.cm)
        # stream.buffer()
        conn = urllib2.urlopen(self.url)
        while True:
            chunk = conn.read(BUFFER_SIZE)
            if not chunk:
                break
            self.cm.write(time.time(), chunk)
