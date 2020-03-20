""" HAROLD BERNIE P. GARCIA
   DATALOG Lab07
   March 18, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""

def M_number(row, begin, end):

    if (begin > end): # If NUMBER is < THAN THE LAST VALUE : RETURN
        return end + 1
    if (begin != row[begin]):
        return begin
    x = int((begin + end) / 2)
    if (row[x] == x):
        return M_number(row, x + 1, end)


A = [0, 1, 2, 3, 5, 6, 7, 8]
B= [1, 2, 3, 4, 6, 11, 17]
C = [0, 1, 2, 3, 4, 5, 6, 7, 8]

K=len(A)
K=len(B)
K=len(C)

print("1st",A)
print("2nd",B)
print("3rd",C)

print(" 1st small missing No.: ", M_number(A, 0, K-1))
print(" 2nd small missing No.: ", M_number(B, 0, K-1))
print(" 3rd small missing No.: ", M_number(C, 0, K-1))