# https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

examples_extension = Extension(name="helloWorld", sources=["helloWorldCython.pyx", "helloWorld.c"])
setup(name="helloWorld", ext_modules=cythonize(examples_extension), cmdclass={'build_ext':build_ext})      # this syntax of "setup" command also works fine
#setup(name="helloWorld", ext_modules=[examples_extension], cmdclass={'build_ext':build_ext})              # this syntax of "setup" command also works fine