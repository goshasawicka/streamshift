#!/usr/bin/env python
import time
import logging
import os
import ConfigParser

from multiprocessing import Process

from streamshift import StreamProcess

config = ConfigParser.ConfigParser()
config.read('./config.cfg')

stations = config.sections()
stations.remove('global')
for station in stations:

    config_setup = config.items(station)

    config_setup.append(("path", config.items("global")[0][1]))
    cp = StreamProcess(config_setup)
    for f in [cp.purge, cp.buffering]:
        Process(target=f).start()
