=============
gevent-egg
=============

This library supply gevent prebuilt egg for python 2.7

Requirements
------------

* sys.version[:3] == '2.7'
* sys.platform in ('win32', 'darwin', 'linux2')
* platform.machine() in ('x86', 'x86_64', 'i686')

Usage
-----

easy_install:

..
    
    easy_install https://github.com/phuslu/gevent-egg/raw/egg/gevent-1.0-py2.7-linux.egg
    
pip

..
    
    pip install git+git://github.com/phuslu/gevent-egg.git@master#egg=gevent

requirements.txt

..
    
    -e git://github.com/phuslu/gevent-egg.git@master#egg=gevent



License
-------
New BSD

