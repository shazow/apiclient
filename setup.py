#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def path(p):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), p)

long_description = ''

try:
    long_description += open(path('README.rst')).read()
    long_description += '\n\n' + open(path('CHANGES.rst')).read()
except IOError:
    pass

version = '1.0.3'

requirements = [
    'urllib3',
]
tests_requirements = requirements + [
    'nose',
]

setup(name='apiclient',
      version=version,
      description="Framework for making good API client libraries using urllib3.",
      long_description=long_description,
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='api client urllib3 keepalive threadsafe http rest',
      author='Andrey Petrov',
      author_email='andrey.petrov@shazow.net',
      url='https://github.com/shazow/apiclient',
      license='MIT',
      packages=['apiclient'],
      install_requires=requirements,
      tests_require=tests_requirements,
      )
