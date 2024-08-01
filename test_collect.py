from sympy import *
x, y, a, b, c, d, const1, const2 = symbols('x y a b c d const1 const2')
expr = a*x + b*x + c*y + d*y + const1 + const2
print(expr)
collected1 = expr.collect(x)
collected2 = collected1.collect(y)
print(collected2)
