# coding=utf-8
import sys
import os
sys.modules["ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))

from .api import *

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Elementary Math Library. (For demonstration purpose only)
"""

__version__ = "0.0.1"
__short_description__ = "Elementary Mathematics."
__author__ = "Max"
__author_email__ = "Max@me.com"
__maintainer__ = "Max"
__maintainer_email__ = "Max@me.com"
__github_username__ = "Max"


def add_two(a):
    """Return a + 2.
    """
    return a + 2

__all__ = [
    "add_one"
]
