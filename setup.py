#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='smsAlert',
    version='1.0.0',
    description="A simple python client for Sms Alert APIs",
    long_description=readme + '\n\n' + history,
    long_description_content_type= 'text/markdown',
    author="Prashant",
    author_email='prashant@cozyvision.com',
    url='https://github.com/smsAlert',
    packages=[
        'smsAlert',
    ],
    package_dir={'smsAlert':
                 'smsAlert'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='smsAlert',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
