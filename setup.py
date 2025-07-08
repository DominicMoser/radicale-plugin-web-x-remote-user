#!/usr/bin/env python3

import os

from setuptools import setup

VERSION = "3.1.6"

package_path = os.path.join(os.path.dirname(__file__), "radicale_web")
web_data = sum((
    [os.path.relpath(os.path.join(root, f), package_path)
     for f in files if not f.startswith(".") and not f.endswith("~")]
    for root, _, files in os.walk(os.path.join(package_path, "web"))), [])

setup(
    name="Radicale_Web",
    version=VERSION,
    description="Radicale Web without logging in",
    author="Dominic",
    author_email="dominic@dmoser.dev",
    url="https://github.com/DominicMoser/radicale-plugin-web-x-remote-user",
    license="GNU GPL v3",
    platforms="Any",
    packages=["radicale_web"],
    package_data={"radicale_web": web_data},
    install_requires=["radicale>=3.1.6"])
