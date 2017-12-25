#!/usr/bin/env python
# coding=utf-8

import sys
from os.path import dirname, join
from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)


with open(join(dirname(__file__), 'VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]


setup(
    name="jqdatasdk",
    version=version,
    description="jqdatasdk<SDK of fetch finance data from JoinQuant>",
    packages=["jqdatasdk", "jqdatasdk.macro_tables"],
    author="JoinQuant",
    author_email="xlx@joinquant.com",
    maintainer="wangchaoyang",
    maintainer_email="wangchaoyang@joinquant.com",
    license='Apache License v2',
    package_data={'': ['*.*']},
    url="https://www.joinquant.com/data",
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


