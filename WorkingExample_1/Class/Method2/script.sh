# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

gcc -c class_example.cpp
ar rcs libclass_example.a class_example.o
python setup.py build_ext --inplace
python test.py