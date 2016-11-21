import logging
import os

class GenericObject(object):

    def getLogger():
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(
            logging.Formatter(
                '[%(levelname)s][%(module)s:%(funcName)s]: %(message)s',
            )
        )
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(console)
        return logger

    logger = getLogger()

