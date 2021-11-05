# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext = Extension(name="pyMultiply", sources=["pyMultiply.pyx"])
setup(name="pyMultiply", ext_modules=cythonize(ext), cmdclass={'build_ext':build_ext})      # this syntax of "setup" command also works fine
#setup(name="pyMultiply", ext_modules=[ext], cmdclass={'build_ext':build_ext})              # this syntax of "setup" command also works fine