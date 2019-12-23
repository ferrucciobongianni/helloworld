#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from subprocess import check_output, CalledProcessError

base_path = os.path.dirname(__file__)


def read(fname):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(base_path, fname)).read()

setup(
    name="helloworld",
    version='0.0',
    author="Ferrucio Bongianni",
    author_email="ferruccio.bongianni@gmail.com",
    description='Hello World',
    entry_points={'console_scripts': ['hello-world = helloworld.cmd:cmd']},
    include_package_data=True,
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=[],
    data_files=[('config', ['README.md'])]
)
