import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def infection_func(sir, t, contact_rate, recovery_rate, life_duration, mortality_rate):
    s, i, r = sir
    s_next = -contact_rate * i * s + (i + r) / (365 * life_duration)
    i_next = contact_rate * i * s - (recovery_rate + mortality_rate) * i - i / (365 * life_duration)
    r_next = recovery_rate * i - r / (365 * life_duration)
    return np.array((s_next, i_next, r_next))

# Total population = 100000
s0 = 99999  # Susceptible
i0 = 1  # Infected
r0 = 0 # Removed (Recovered)
Re = 3.26  # effective reproductive number
D = 14  # duration of illness
life = 73  # mean life duration in Russia
mortality = 0.022 # illness mortality rate
recovery_rate = 1/D
mortality_rate = mortality / D # illness mortality rate per day
contact_rate = (Re / s0) / D

sir0 = np.array((s0, i0, r0))
t = np.linspace(0, 600, 1000)
plt.figure(figsize=(14, 6))
сolors_in_plot = ['blue', 'orange', 'green', 'red']
linestyles = ['-', '--', '-.', ':']
for i in range(0, 4):
    contact_rate_var = contact_rate * (1 - 0.2 * i)
    for j in range(0, 4):
        recovery_rate_var = 1 / (D - j)
        variables_tuple = (contact_rate_var, recovery_rate_var, life, mortality_rate)
        infection = integrate.odeint(func=infection_func, y0=sir0, t=t, args=variables_tuple)
        susceptible = infection[:, 0]
        infected = infection[:, 1]
        recovered = infection[:, 2]
        plt.plot(t, infected,
                 label=f"Contact rate = {100 * round(1 - 0.2 * i, 1)}%, Illness duration = {round(D - j)}",
                 linestyle=linestyles[j], color=сolors_in_plot[i], linewidth=2)


plt.xlabel('Days', fontsize=15)
plt.ylabel('People', fontsize=15)
plt.title('Infected people dependence on contact rate and illness duration', fontsize=15)
plt.legend()

plt.show()
#plt.savefig('Infected people dependence on contact rate and illness duration.png', bbox_inches='tight')
