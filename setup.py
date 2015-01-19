#! /usr/bin/env python

from distutils.core import setup

DESCRIPTION = """\
esptools is a set of command-line utilities for managing files on LUA-Based
ESP8266 modules.

It was created by David Lyon from clixx.io

"""

def run():
    setup(name="esptools",
        version="0.1.0",
        description="Command line tools for managing LUA ESP8266 modules",
        url="https://github.com/clixx-io/esptools/",
        license="GNU GPL Version 2",
        author="David Lyon",
        maintainer_email="support@clixx.io",
        packages=["esptools"],
        long_description=DESCRIPTION,
        download_url=
            "http://sourceforge.net/project",
        platforms=["OS Independent"],
        classifiers=[OC
            "Development Status :: 1 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )

if __name__ == "__main__":
    run()

