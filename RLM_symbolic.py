from sympy import *
v_g, i1, i1p, R1, L1, dt = symbols('v_g i1, i1p, R1, L1 dt')
M = symbols('M')
i2, i2p, R2, L2 = symbols('i2, i2p, R2, L2')

expr1 = -v_g + i1*R1 + L1*(i1p-i1)/dt - M*(i2p-i2)/dt
expr2 = i2*R2 + L2*(i2p-i2)/dt - M*(i1p-i1)/dt

print(expr1)
print(expr2)

expr1 = Poly(expr1, i1p, i2p)
expr2 = Poly(expr2, i1p, i2p)

expr1_coeffs = expr1.coeffs()
expr2_coeffs = expr2.coeffs()

A11 = expr1_coeffs[0]
A12 = expr1_coeffs[1]
b1 = -expr1_coeffs[2]

A21 = expr2_coeffs[0]
A22 = expr2_coeffs[1]
b2 = -expr2_coeffs[2]

A = [[A11, A12], [A21, A22]]
b = [b1, b2]

print(A[0])
print(A[1])
print(b)



