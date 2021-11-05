# https://stackoverflow.com/questions/2105508/wrap-c-lib-with-cython/2106051

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = Extension(name="ExmpAddMult", sources=["ExmpAddMultCy.pyx", "ExmpAddMult.cpp"], language="c++")
setup(name="ExmpAddMult", ext_modules=cythonize(ext_modules), cmdclass={'build_ext': build_ext})                 # this syntax of "setup" command also works fine
#setup(name="ExmpAddMult", ext_modules=[ext_modules], cmdclass={'build_ext': build_ext})                         # this syntax of "setup" command also works fine