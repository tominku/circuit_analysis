import sympy as sym
x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

x1 = 2*x1 + x2
x2 = 3

print(x1)
result = x1.subs(x2, 3)
print(result)
