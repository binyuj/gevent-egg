#!/usr/bin/env python

import sys
import os
from distutils.core import setup

if sys.version[:3] not in ('2.6', '2.7'):
    raise NotImplementedError("Sorry, you need at Python 2.6/2.7 to use gevent-egg.")
    
if sys.maxunicode == 65535:
    raise NotImplementedError("Sorry, you need at Python UCS4 to use gevent-egg.")

if sys.platform not in ('linux2', 'darwin', 'win32'):
    raise NotImplementedError("Sorry, you need at Linux/MacOS/WinNT to use gevent-egg.")

import gevent

setup(name='gevent',
      version=gevent.__version__,
      description='Coroutine-based network library',
      long_description=gevent.__doc__,
      author='Denis Bilenko',
      author_email='denis.bilenko@gmail.com',
      url='http://gevent.org/',
      packages=['gevent', 'greenlet'],
      package_data={'gevent': ['*.so'], 'greenlet': ['*.so']},
      #cmdclass=dict(build_ext=my_build_ext, sdist=sdist),
      license='MIT',
      platforms='any',
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7",
                   "Operating System :: MacOS :: MacOS X",
                   "Operating System :: POSIX",
                   "Operating System :: Microsoft :: Windows",
                   "Topic :: Internet",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Intended Audience :: Developers",
                   "Development Status :: 4 - Beta"],)
