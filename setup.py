#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='m3-project',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'django==1.11.28',
        'm3-builder==1.2.0',
        'm3-objectpack==2.2.25',
    ],
    dependency_links=[
        'http://pypi.bars-open.ru/simple/',
    ]
)