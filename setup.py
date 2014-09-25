from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import setup, find_packages

import perform

perform_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(
        name="perform",
        version=perform.__version__,
        description="Easily call processes from python",
        long_description=perform.__doc__,
        url="http://github.com/BenDoan/perform",
        author="Ben Doan",
        author_email="ben@bendoan.me",
        license="MIT",
        py_modules = ['perform'],
        classifiers=perform_classifiers
)
