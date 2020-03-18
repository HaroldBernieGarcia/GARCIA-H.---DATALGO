"""
DATALOG lab05
Feb. 19, 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(10*9)

# corresponding y axis values
y1 = 8 * n
y2 = 4 * n * n
y3 = 2 ** n ** 2
y4 = n * 3
y5 = 2 * n

plt.plot(n, y1)
plt.plot(n, y2)
plt.plot(n, y3)
plt.plot(n, y4)


plt.xlabel('Log')
plt.ylabel('Log')
plt.title("PLOT OF R-3.1a\nDATALgo")
plt.xscale('log')
plt.yscale('log')

plt.show()