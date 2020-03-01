#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monitor",
    version="0.1",
    author="Brandon Boykin",
    author_email="bboykin87@gmail.com",
    description="Package to monitor if servers are available to connect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bboykin87/monitor.py",
    packages=['monitor.modules'],
    #package_dir={'monitor' : 'modules'},
    package_data={'monitor.modules' :['monitor/modules/filecheck.py','monitor/modules/logs.py']},
    scripts=['monitor/scan.py'],
    classifiers=[
        "Programming Languaage :: Python :: 3",
        "Operating System :: Linux"
    ],
    python_requires='>=3.6',
)
