import numpy as np
import numpy.linalg as LA

# [L1/dt, -M/dt]
# [-M/dt, L2/dt]
# [-(-L1*i1 + M*i2 + R1*dt*i1 - dt*v_g)/dt, -(-L2*i2 + M*i1 + R2*dt*i2)/dt]

dt = 0.01
L1 = 12
L2 = 12
M = 4
R1 = 20
R2 = 20
v_g_mag = 5
v_g = v_g_mag
is_input_wave = False
#is_input_wave = True

A = np.array([[L1/dt, -M/dt], [-M/dt, L2/dt]])
print(A)

i = 0

i1_list = []
i2_list = []
v_g_list = []
t_list = []
i1 = 0
i2 = 0
t_on = 1
for step in range(800): 
    t = dt*step   
    if t > t_on:
        v_g = v_g_mag  
        if is_input_wave:
            freq = 1
            v_g = v_g_mag*np.sin(2*np.pi*freq*(t-t_on))
    else:
        v_g = 0                  
    
    b = np.array([-(-L1*i1 + M*i2 + R1*dt*i1 - dt*v_g)/dt, -(-L2*i2 + M*i1 + R2*dt*i2)/dt])        
    i = LA.solve(A, b)
    
    i1 = i[0]
    i2 = i[1]    
    i1_list.append(i1)
    i2_list.append(i2)
    v_g_list.append(v_g)
    t_list.append(t)
    #print(f'a: {(-R*dt/L) + 1}, b: {v_g*dt/L}')

import matplotlib.pyplot as plt
i1_arr = np.array(i1_list)
i2_arr = np.array(i2_list)
v_g_arr = np.array(v_g_list)
t_arr = np.array(t_list)
plt.plot(t_arr, i1_arr, label='I1 (t)')
plt.plot(t_arr, i2_arr, label='I2 (t)')
v_g_plot_scale = 0.05
#plt.plot(t_arr, v_g_plot_scale*v_g_arr, label=f'{v_g_plot_scale} * V_g(t)')
plt.grid(True)
plt.legend()
plt.show()
