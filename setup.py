#!/usr/bin/env python

from distutils.core import setup

setup(name='Leadreader',
    version='0.1',
    description='Leadsheet Analysis',
    author='Ian Baker <ian@sonic.net>, Serene Han <keroserene@gmail.com>, Ken Hirsh <ken.hirsh@gmail.com>',
    author_email='ian@sonic.net',  #accepts only one email
    url='https://github.com/raindrift/leadreader',
    packages=['leadreader'],
    entry_points = {
        'console_scripts': ['leadreader=leadreader.cli:main'],
    }
)
