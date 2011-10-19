#!/usr/bin/env python

from distutils.core import setup


try:
    import setuptools
except ImportError, _:
    pass # No 'develop' command, oh well.


version = '1.0.1'

requirements = [
    'urllib3',
]
tests_requirements = requirements + [
    'nose',
]

setup(name='apiclient',
      version=version,
      description="Framework for making good API client libraries using urllib3.",
      long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read(),
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
      requires=requirements,
      tests_require=tests_requirements,
      )
