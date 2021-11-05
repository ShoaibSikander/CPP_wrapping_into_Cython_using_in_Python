# https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/

gcc -c helloWorld.c
ar rcs libhelloWorld.a helloWorld.o
python setup.py build_ext --inplace
python main.py