# http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

import pyMultiply

var1 = 3
var2 = 2

sumResult = pyMultiply.pyTestSum(var1, var2)
print("Sum Result: ", sumResult)

sumResult = pyMultiply.cpSum(var1, var2)
print("Sum Result: ", sumResult)

multiplicationResult = pyMultiply.pyTestMultiply(var1, var2)
print("Multiplication Result: ", multiplicationResult)

# uncommenting following commands would produce an error because "pyMultiply" function cannot be called from Python
#multiplicationResult = pyMultiply.cMultiply(var1, var2)
#print("Multiplication Result: ", multiplicationResult)
