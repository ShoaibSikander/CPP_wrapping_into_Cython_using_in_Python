# http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html

from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = Extension(name="rect", sources=["rect.pyx", "Rectangle.cpp"], language="c++")
setup(name = "rect", ext_modules=cythonize(ext_modules), cmdclass={'build_ext': build_ext})     # this syntax of "setup" command also works fine
#setup(name = "rect", ext_modules=[ext_modules], cmdclass={'build_ext': build_ext})             # this syntax of "setup" command also works fine
