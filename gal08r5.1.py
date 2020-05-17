""" HAROLD BERNIE P. GARCIA
   DATALOG Lab07
   March 18, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

import sys
data = []
cur = 0
for k in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    if b > cur and a > 0:
        cur = b
        print('''Exausted when lenth = {0}'''.format(a - 1))
    data.append(None)