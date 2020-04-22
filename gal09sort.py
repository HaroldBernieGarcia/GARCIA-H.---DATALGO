""" HAROLD BERNIE P. GARCIA
   DATALOG Lab09
   APRIL 23, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""



def encrypt(string, shift):
    cipher = ''

    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

a = ('DonBoscoTechnicalCollege')
text = a
s = 3
print("encryptED CODE: ", encrypt(text, s))
print("reSULT CODE: ", text)
