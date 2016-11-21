import os
import time

from streamshift.util import GenericObject
from streamshift.stream import Stream, ChunkManager

class StreamProcess(GenericObject):

    def __init__(self, config):
        self.url = config[0][1]
        self.offset = config[1][1]
        self.path = config[2][1]
        self.logger.info("New process %d" % os.getpid())
        self.cm = ChunkManager(self.path, self.url)

    def purge(self):
        self.logger.info("Purging")
        while True:
            time.sleep(1)
            stream = Stream(self.url, self.cm)
            stream.purge()

    def buffer(self):
        self.logger.info("Buffering")
        stream = Stream(self.url, self.cm)
        stream.buffer()
