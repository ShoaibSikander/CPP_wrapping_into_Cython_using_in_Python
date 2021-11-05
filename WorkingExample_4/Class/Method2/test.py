# https://stackoverflow.com/questions/2105508/wrap-c-lib-with-cython/2106051

import ExmpAddMult

pyObj = ExmpAddMult.PyComputation()

num1 = 4
num2 = 5

resultAdd = pyObj.performAdd(num1,num2)
print("Addition: ", resultAdd)

resultMultiply = pyObj.performMultiply(num1,num2)
print("Multiplication: ", resultMultiply)
