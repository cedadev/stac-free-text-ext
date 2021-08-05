# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '05 Aug 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

from setuptools import setup, find_namespace_packages

with open("README.md") as readme_file:
    _long_description = readme_file.read()

setup(
    name='stac_fastapi_freetext',
    description='Free-text extension for STAC. Developed for use with the stac-fastapi framework',
    author='Richard Smith',
    url='https://github.com/cedadev/stac-free-text-ext',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    license='BSD - See LICENSE file for details',
    packages=find_namespace_packages(),
    python_requires='>=3.5',
    install_requires=[
        'attr',
        'fastapi',
        'stac-fastapi.types',
    ],
)