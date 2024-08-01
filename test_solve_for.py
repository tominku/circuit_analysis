from sympy import *
v_g, i1, i1p, R1, L1, dt = symbols('vg i1, i1p, R1, L1 dt')

expression = Eq(-v_g + i1*R1 + L1*(i1p-i1)/dt, 0)
print(expression)

result = solve(expression, i1p)[0]
print(result)
