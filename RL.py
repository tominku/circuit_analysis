import numpy as np

R = 20
L = 8
v_g_mag = 5
dt = 0.01

is_input_wave = True
#is_input_wave = False

i = 0

i_list = []
v_g_list = []
t_list = []
for step in range(800): 
    t = dt*step   
    v_g = v_g_mag
    if is_input_wave:
        freq = 1
        v_g = v_g_mag*np.sin(2*np.pi*freq*t)
    i = ((-R*dt/L) + 1)*i + v_g*dt/L    
    i_list.append(i)
    v_g_list.append(v_g)
    t_list.append(t)
    #print(f'a: {(-R*dt/L) + 1}, b: {v_g*dt/L}')

import matplotlib.pyplot as plt
i_arr = np.array(i_list)
v_g_arr = np.array(v_g_list)
t_arr = np.array(t_list)
plt.plot(t_arr, i_arr, label='I (t)')
v_g_plot_scale = 0.05
plt.plot(t_arr, v_g_plot_scale*v_g_arr, label=f'{v_g_plot_scale} * V_g(t)')
plt.grid(True)
plt.legend()
plt.show()
