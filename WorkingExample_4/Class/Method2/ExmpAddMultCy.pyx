# distutils: language = c++

cimport ExmpAddMult

cdef class PyComputation:
    cdef computation performComputation

    def performAdd(self, var1, var2):
        return self.performComputation.add(var1, var2)

    def performMultiply(self, var1, var2):
        return self.performComputation.multiply(var1, var2)