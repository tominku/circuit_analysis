from sympy import *
v_g, i1, i1p, R1, L1, dt = symbols('vg i1, i1p, R1, L1 dt')
M = symbols('M')
i2, i2p, R2, L2 = symbols('i2, i2p, R2, L2')

expr1 = -v_g + i1*R1 + L1*(i1p-i1)/dt - M*(i2p-i2)/dt
expr2 = i2*R2 + L2*(i2p-i2)/dt - M*(i1p-i1)/dt

print(expr1)
print(expr2)

expr1 = expr1.collect(dt)
print(expr1)