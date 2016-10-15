#!/usr/bin/env python

import os
from setuptools import setup

from jqp import __version__


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name='jqp',
    version=__version__,
    description='JSON processor with Python one-liner',
    long_description=read('README.rst'),
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    url='https://github.com/unnonouno/jqp',
    license='MIT License',
    packages=['jqp'],
    scripts=['scripts/jqp'],
    test_suite='tests',
    classifiers=[
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Information Technology',
        'Topic :: Utilities',
    ],
)
