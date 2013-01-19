#!/usr/bin/env python
import jsonhacker
import distribute_setup
distribute_setup.use_setuptools()

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "json-hacker", 
    version = jsonhacker.get_version(),
    description = "A cross-platform GUI editor for JSON files.",
    long_description = read("README.rst"),
    author = "Micah Carrick",
    author_email = "micah@quixotix.com",
    url = "https://www.github.com/MicahCarrick/json-hacker",
    packages = find_packages(),
    scripts=[os.path.join("bin", script) for script in os.listdir("./bin")],
    license = "New BSD License",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Text Editors",
        "License :: OSI Approved :: BSD License",
    ],
    #test_suite = "jsonhacker.test"
)

