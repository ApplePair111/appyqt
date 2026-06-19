from appyqt.asyncTools import *
import time

def myFunction(arg1, arg2):
    time.sleep(3)
    return arg1 + arg2

runFunctionAsync(myFunction, "Add two numbers", 1, 3)
