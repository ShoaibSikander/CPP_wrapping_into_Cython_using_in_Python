# https://stackoverflow.com/questions/2105508/wrap-c-lib-with-cython/2106051

gcc -c ExmpAddMult.cpp
ar rcs libExmpAddMult.a ExmpAddMult.o
python setup.py build_ext --inplace
python test.py