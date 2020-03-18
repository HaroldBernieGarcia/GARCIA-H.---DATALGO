""" HArold Bernie P. Garcia
DATALOG
March. 4 , 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
def value_test (x):
    # this function fails if the list length is 0 
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)

print(value_test([9,8,7,6,5,4,3,2,-1,1,11,12,54,13,14,15,16,17,18,19,20,32]))
print("minimum,maximum")