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

    ORDER = f(a)>0 #this tells us which to assign c to, since depending on which of a and b is positive, who is assigned c is swapped.
    c = (b+a)/2

    while abs(f(c)) > EPS:
        if f(c) > 0:
            if ORDER:
                a = c
            else:
                b = c
        else:
            if ORDER:
                b = c
            else:
                a = c

        c = (b+a)/2

    return c