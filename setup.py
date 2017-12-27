#!/usr/bin/env python
# coding=utf-8

import sys
from os.path import dirname, join
from pip.req import parse_requirements

from setuptools import (
    setup
)


with open(join(dirname(__file__), 'VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]


setup(
    name="My_first_program",
    version=version,
    description="It's My_first_program>",
    packages=["My_first_program"],
    author="Max Bai",
    author_email="familybjp@gmail.com",
    maintainer="MaxBai",
    maintainer_email="familybjp@gmail.com",
    license='Apache License v2',
    package_data={'': ['*.*']},
    url="https://github.com/MaxBai6/My_first_program",
    install_requires=requirements,
    zip_safe=False,
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)


