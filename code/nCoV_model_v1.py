#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interact_manual


# In[2]:


df_time = pd.read_csv("../Assets/zeros_JHU_Data_2020.02.07_PM.csv")


# In[3]:


df_total = pd.read_csv("../Assets/JHU_SID_2020.02.07.csv")


# In[4]:


df_total.head()

N, R0, D0, I0, S0 = (5638676, 0, 0, 30, 5638646)


# In[107]:


duration_slider = widgets.IntSlider(min=0, max=20, step=1, description='Duration (D):',value=14)
duration_slider


# In[108]:


Rnaught_slider = widgets.FloatSlider(value= 2, min=0, max=3, step=0.1, description='R0:')
Rnaught_slider


# In[110]:


duration = int(duration_slider.value)
Rnaught = float(Rnaught_slider.value)

# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
gamma = float(1/duration) 
beta = float(Rnaught*gamma)

# A grid of time points (in days)
t = np.linspace(0, 500, 500)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
#ax.plot(t, S/1000000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000000, 'r', alpha=0.5, lw=2, label='Infected')
#ax.plot(t, R/1000000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Number (M)')
#ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()


# In[ ]:




