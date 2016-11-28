import os
import time

from streamshift.util import GenericObject
from streamshift.stream import Stream, ChunkManager

class StreamProcess(GenericObject):

    def __init__(self, config):
        self.url = config[0][1]
        self.buffer = config[1][1]
        self.shift = config[2][1]
        self.path = config[3][1]

        self.logger.info("New process %d" % os.getpid())
        self.cm = ChunkManager(self.path, self.url, self.buffer, self.shift)

    def purge(self):
        self.logger.info("Purging")
        while True:
            # print ("### process.py, StreamProcess purge in while loop")

            time.sleep(1)

            # print ("###### process.py, StreamProcess purge after sleep")
            stream = Stream(self.url, self.cm)
            # print ("### process.py, StreamProcess stream created")

            stream.purge()

    def buffering(self):
        self.logger.info("Buffering")
        stream = Stream(self.url, self.cm)
        stream.buffer()
