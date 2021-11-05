# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

#gcc -c class_example.cpp -o class_example.o		# not needed
#gcc -shared class_example.o -o class_example.so	# not needed
python setup.py build_ext --inplace
python test.py