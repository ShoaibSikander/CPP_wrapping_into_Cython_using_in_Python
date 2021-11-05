# a function that can be called both in C and python
cpdef cpSum(double a, double b):
    return a + b

# a function that can be called from C
cdef cMultiply(double a, double b):
    return a * b

# just a notmal python function
def pyTestSum(var1, var2):
    return cpSum(var1, var2)

# just a notmal python function
def pyTestMultiply(var1, var2):
    return cMultiply(var1,var2)