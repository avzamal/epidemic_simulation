import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def infection_func(sir, t, contact_rate, recovery_rate, life_duration, mortality_rate):
    s, i, r = sir
    s_next = -contact_rate * i * s + (i + r) / (365 * life_duration)
    i_next = contact_rate * i * s - (recovery_rate + mortality_rate) * i - i / (365 * life_duration)
    r_next = recovery_rate * i - r / (365 * life_duration)
    return np.array((s_next, i_next, r_next))


plt.rcParams.update({'font.size': 15})

# Total population = 100000
s0 = 99999  # Susceptible
i0 = 1  # Infected
r0 = 0  # Removed (Recovered)
Re = 3.26  # effective reproductive number
D = 14  # duration of illness
life = 73  # mean life duration in Russia
mortality = 0.022 # illness mortality rate
recovery_rate = 1/D
mortality_rate = 0.022 / D # illness mortality rate per day
contact_rate = (Re / s0) / D

sir0 = np.array((s0, i0, r0))
t = np.linspace(0, 300, 1000)

plt.figure(figsize=(6, 6))
variables_tuple = (contact_rate, recovery_rate, life, mortality_rate)
infection = integrate.odeint(func=infection_func, y0=sir0, t=t, args=variables_tuple)
susceptible = infection[:, 0]
infected = infection[:, 1]
recovered = infection[:, 2]


plt.plot(t, susceptible, label='Susceptible', linewidth=4)
plt.plot(t, infected, label='Infected', linewidth=4)
plt.plot(t, recovered, label='Recovered', linewidth=4)
plt.xlabel('Days')
plt.ylabel('People')
plt.title('Infection simulation')
plt.legend()

plt.show()
# plt.savefig('plot.png', bbox_inches='tight')
