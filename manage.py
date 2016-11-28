#!/usr/bin/env python
import time
import logging
import os
import ConfigParser

from multiprocessing import Process

from streamshift import StreamProcess

config = ConfigParser.ConfigParser()
config.read('./config.cfg')
# print ("### manage.py, config created")

stations = config.sections()
stations.remove('global')
for station in stations:
    # print ("### manage.py, iterate in stations")

    config_setup = config.items(station)

    config_setup.append(("path", config.items("global")[0][1]))

    cp = StreamProcess(config_setup)

    for f in [cp.buffering, cp.purge]:
        # print ("### manage.py, start processes")
        Process(target=f).start()
