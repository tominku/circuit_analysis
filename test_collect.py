from sympy import *
x, y, a, b, c, d = symbols('x y a b c d')
expr = a*x + b*x + c*y + d*y
print(expr)
collected1 = expr.collect(x)
collected2 = collected1.collect(y)
print(collected2)