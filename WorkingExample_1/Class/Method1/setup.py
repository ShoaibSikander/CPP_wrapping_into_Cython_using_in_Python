# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = Extension(name="pyCar", sources=["pyCar.pyx", "class_example.cpp"], language="c++")
setup(name="pyCar", ext_modules=cythonize(ext_modules), cmdclass={'build_ext':build_ext})      # this syntax of "setup" command also works fine
#setup(name="pyCar", ext_modules=[ext_modules], cmdclass={'build_ext':build_ext})              # this syntax of "setup" command also works fine