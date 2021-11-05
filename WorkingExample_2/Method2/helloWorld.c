// https://stavshamir.github.io/python/making-your-c-library-callable-from-python-by-wrapping-it-with-cython/

#include <stdio.h>

#include "helloWorld.h"

void functionHelloWorld(const char *name) {
    printf("hello %s\n", name);
}