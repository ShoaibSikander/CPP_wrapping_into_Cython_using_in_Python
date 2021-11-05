cdef extern from "ExmpAddMult.h" namespace "calculator":
    cpdef cppclass computation:
        int add(int a,int b)
        int multiply(int a,int b)