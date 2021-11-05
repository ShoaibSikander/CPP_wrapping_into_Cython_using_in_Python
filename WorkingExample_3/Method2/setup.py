# http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html

from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = Extension(name="rect", sources=["rect.pyx"], language="c++", extra_objects=["libRectangle.a"])                                    # this syntax of "Extension" command also works fine
#ext_modules = Extension(name="rect", sources=["rect.pyx"], language="c++", libraries=["Rectangle"], library_dirs=["."], include_dirs=["."])    # this syntax of "Extension" command also works fine

setup(name = "rect", ext_modules=cythonize(ext_modules), cmdclass={'build_ext': build_ext})     # this syntax of "setup" command also works fine
#setup(name = "rect", ext_modules=[ext_modules], cmdclass={'build_ext': build_ext})             # this syntax of "setup" command also works fine
