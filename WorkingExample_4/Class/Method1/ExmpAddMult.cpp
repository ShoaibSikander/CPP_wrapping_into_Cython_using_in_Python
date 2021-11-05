// https://stackoverflow.com/questions/2105508/wrap-c-lib-with-cython/2106051

#include "ExmpAddMult.h"

using namespace calculator;

int computation::add(int a, int b)
{
    return a+b;
}

int computation::multiply(int a, int b)
{
    return a*b;
} 