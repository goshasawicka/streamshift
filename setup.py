import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="streamshift",
    version="0.0.1",
    author="Gosha Sawicka",
    author_email="mal.galazka@gmail.com",
    description=("Buffer audio streams and serve them back with a user-defined offset"),
    license="MIT",
    keywords="radio audio stream",
    url="https://github.com/patyk/streamshift",
    packages=['streamshift', 'tests'],
    long_description=read('README.md'),
    classifiers=[],
)
