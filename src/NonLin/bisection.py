import sys
from collections.abc import Callable

EPS = 1E-6

def bisection(a,b,f:Callable):
    
    # checks for obvious issues
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b

    # checks for validity
    if f(a) * f(b) > 0:
        print("Start and end values with this function iare not valid for application of bisection method, either change limit values or function")
        sys.exit()

    c = (b+a)/2

    while abs(f(c)) > EPS:
        if f(a)*f(c) < 0:
            b = c
        elif f(b)*f(c) < 0:
            a = c
        c = (b+a)/2

    return c