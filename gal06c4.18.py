""" HArold Bernie P. Garcia
DATALOG
March. 4 , 2020
I have neither received nor provided any help on this (exercice) activity,
nor have I concealed any violation of the Honor Code.
"""
string =  input("Enter Word/Text:") # input any text to test:
vowels=0
for i in string:                    # create a variable to define vowels
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): # create selection for variable
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)                       # print numbers of vowels

consonante=0
for j in string:                     # create a variable to define vowels
      if(j=='b' or j=='c' or j=='c' or j=='d' or j=='f' or j=='g' or j=='h' or j=='j' or j=='k' or j=='l'or j=='l' or j=='m' or j=='n' or j=='p' or j=='q'or j=='r' or j=='s' or j=='t' or j=='v' or j=='w'or j=='x' or j=='y' or j=='z'):
         # ^ create selection for variable
            consonante=consonante+1
print("Number of vowels are:")
print(consonante)                    # print numbers of consonant