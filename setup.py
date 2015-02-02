#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

classifiers = [
    "Framework :: Bottle",
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development']

description = "Boilerplate code for new Bottle projects"
try:
    long_description = open('README.rst').read()
except:
    long_description = description

url = 'https://github.com/avelino/bottle-boilerplate'

setup(name='bottle-boilerplate',
      version=0.2,
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      keywords='bottle boilerplate startproject doc',
      author="Thiago Avelino",
      author_email="thiago@avelino.xxx",
      url=url,
      download_url="{0}/tarball/master".format(url),
      license="MIT",
      install_requires=REQUIREMENTS,
      entry_points={
          'console_scripts': ["bottle = bottle_boilerplate:main"]
      },
      include_package_data=True,
      zip_safe=False)
