# https://stackoverflow.com/questions/2105508/wrap-c-lib-with-cython/2106051

import ExmpAddMult

resultAdd = ExmpAddMult.add(4,5)
print("Addition: ", resultAdd)

resultMultiply = ExmpAddMult.multiply(4,5)
print("Multiplication: ", resultMultiply)
