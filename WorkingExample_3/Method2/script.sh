# http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html

gcc -c Rectangle.cpp
ar rcs libRectangle.a Rectangle.o
python setup.py build_ext --inplace
python test.py