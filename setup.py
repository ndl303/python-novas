# -*- coding: utf-8 -*-

import codecs
import os
import platform
from setuptools import setup
from distutils.core import Extension

include_dirs      =[]
library_dirs      =[]
libraries         =[]
extra_compile_args=[]
extra_link_args   =[]
extra_objects     =[]
c_sources         =[ 'Cdist/cio_file.c',
                     'Cdist/eph_manager.c',
                     'Cdist/novas.c',
                     'Cdist/novascon.c',
                     'Cdist/nutation.c',
                     'Cdist/readeph0.c',
                     'Cdist/solsys1.c'
                   ]
system = platform.system().lower()
if 'darwin' in system:
     extra_compile_args: ['-arch', 'i386', '-arch', 'x86_64', '-O2', '-Wall', '-fPIC']
elif 'windows' in system:
     c_sources.append('Cdist/windows_specifics/windows_dllmain.cpp')
     c_sources.append('Cdist/windows_specifics/pyinit_libnovas.c')
     extra_link_args = [r'/DEF:"Cdist\\windows_specifics\\windows_dllexports.def"', '/DLL']
else:      
     extra_compile_args = ['-O2', '-Wall', '-fPIC']

   
extension_module = Extension(    name               = 'novas.libnovas',
                                 sources            = c_sources,
                                 include_dirs       = include_dirs,
                                 library_dirs       = library_dirs,
                                 libraries          = libraries,
                                 extra_compile_args = extra_compile_args,
                                 extra_link_args    = extra_link_args,
                                 extra_objects      = extra_objects
                            )
setup(
    name                 = 'novas_py',
    version              = '3.1.1.5',
    description          = "Python wrappers for the US Naval Observatory's NOVAS-C package",
    author               = 'Eric G. Barron',
    author_email         = "%(firstdotlast)s@%(place)s" % {'firstdotlast': 'eric.barron', 'place': 'usno.navy.mil'},
    maintainer           = 'Eric G. Barron',
    maintainer_email     = "%(firstdotlast)s@%(place)s" % {'firstdotlast': 'eric.barron', 'place': 'usno.navy.mil'},
    url                  = 'http://www.usno.navy.mil/USNO/astronomical-applications/software-products/novas',
    download_url         = 'http://www.usno.navy.mil/USNO/astronomical-applications/software-products/novas',
    packages             = ['novas', 'novas.compat', 'novas.tests'],
    package_dir          = { 'novas'       : 'novas_py' },
    data_files           = [], 
    ext_modules          = [extension_module],
    include_package_data = False,
)

