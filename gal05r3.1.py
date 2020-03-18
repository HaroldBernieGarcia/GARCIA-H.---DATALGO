""" Harold Bernie P. Garcia
DATALOG lab05
Feb. 19, 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10^9)

# corresponding y axis values 
y1 = 8 * x
y2 = 4 *x* x
y3 = 2**x**2
y4 = x**3
y5 = 2**x

plt.plot(x, y1, label="8x")
plt.plot(x, y2, label="4n Log(n)")
plt.plot(x, y3, label="2n^2")
plt.plot(x, y4, label="n^3")


plt.xlabel('Log X AXIS')
plt.ylabel('Log Y AXIs')
plt.title("PLOT OF R-3.1\nDATALgo FEB. 19 ,2020\n i3-2365M cpu @ 1.40GHz ")
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.show() 