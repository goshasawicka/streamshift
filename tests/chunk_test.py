import unittest
from streamshift.stream import *


class ChunkTest(unittest.TestCase):

    def setUp(self):
        self.cm = ChunkManager(
            "/tmp/",
            "http://stream3.polskieradio.pl:8904/",
            60
        )
        self.chunk = Chunk(time.time(), self.cm.path, self.cm)

    def test_write_read_delete(self):
        #write
        self.chunk.write("test input")
        with open(self.chunk.filepath, "r") as file:
            f = file.read()
            self.assertTrue(f, "test input")
        # read
        file = self.chunk.read()
        self.assertTrue(file, "test input")
        # delete
        self.chunk.delete()
        assert not os.path.exists(self.chunk.filepath)
        self.chunk.delete()
        self.assertRaises(Exception, self.chunk.delete())
