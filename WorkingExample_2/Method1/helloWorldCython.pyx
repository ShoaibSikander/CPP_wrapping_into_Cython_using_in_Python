cdef extern from "helloWorld.h":
    void functionHelloWorld(const char *name)

def py_functionHelloWorld(name: bytes) -> None:
    functionHelloWorld(name)
