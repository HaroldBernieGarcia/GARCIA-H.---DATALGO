""" HAROLD BERNIE P. GARCIA
   DATALOG :   Create a Linked List Search

   May 11, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.

"""

class ArrayStack:

    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def transfer(s, t):
    for n in range(len(s)):
        t.append(s.pop())
    return t


s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.push(15)
print( "S Stack's" ,s._data)
print(len(s))
T = []

print("T Stack's",transfer(s,T))
print(len(T))