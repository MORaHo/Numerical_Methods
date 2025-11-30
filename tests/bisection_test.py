from src.Maths import cos
from src.NonLin import bisection

func = lambda x: cos(x)
print(bisection(-3,0,func))