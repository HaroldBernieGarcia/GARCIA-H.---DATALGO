""" HAROLD BERNIE P. GARCIA
   DATALOG :  Lab 11 Queue

   May 11, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.

"""

class ArrayQueue:
    Set_value = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.Set_value
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):

        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


Value = ArrayQueue()
print(Value.enqueue(5))
print(Value.enqueue(3))
print(Value.dequeue())
print(Value.enqueue(2))
print(Value.enqueue(8))
print(Value.dequeue())
print(Value.enqueue(9))
print(Value.enqueue(1))
print(Value.dequeue())
print(Value.enqueue(7))
print(Value.enqueue(6))
print(Value.dequeue())
print(Value.enqueue(4))
print(Value.dequeue())