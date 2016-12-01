import os
from setuptools import setup

setup(
    name="streamshift",
    version="0.0.9",
    author="Gosha Sawicka",
    author_email="mal.galazka@gmail.com",
    description=("Buffer audio streams and serve them back with a user-defined offset"),
    license="MIT",
    keywords="radio audio stream",
    url="https://github.com/patyk/streamshift",
    packages=['streamshift', 'tests'],
    classifiers=[],
    py_modules=['streamshift'],
    install_requires=[
        'Click',
        ],
    entry_points='''
        [console_scripts]
        streamshift=streamshift.cli:cli
        '''
)
