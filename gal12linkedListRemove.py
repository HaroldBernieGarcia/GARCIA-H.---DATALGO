""" HAROLD BERNIE P. GARCIA
   DATALOG :   Create a Linked List Remove

   May 11, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.


    Write a remove method that takes an element and removes it from the linked list.
    Notes:

    The length of the list should decrease by one every time an element is removed from the linked list.
    Include your add method from the previous exercise.

   """

class Node:
    def __init__(self, element=None):
        self._element = element
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def head(self):
        return self._head._element

    def traverse(self):
        current = self._head
        while current:
            print(f'{current._element} ', end="")
            current = current._next
        print('')

    # include your add method here *********************************************************************************************************************************

    def remove(self, element):

        # Change code below this line
        Value = self._head                                                         # Create a new node, Put in the data,Set next as None
                                                                                   # if there are elements in the linked list

        if Value is not None:                                                      # If the Linked List is empty, then make the new node as head
            if Value._element == element:
                self._head = Value._next
                return
        while Value is not None:                                                   # for Element list
            if Value._element == element:
                break
            x = Value
            Value = Value._next                                                    # the element is None or Void
            return None                                                           # for element that cant be found will return as "None_"
        x._next = Value._next
        pass

    def add(self, element):
        Set = Node(element)                                                        # Create a new node, Put in the data,Set next as None
        if self._head is None:
            self._head = Set                                                       # list Linked List
            self._size += 1

            return
        Data = self._head
        while Data._next:
            Data = Data._next                                                      # Create a Variable , Put in the data
        Data._next = Set
        self._size += 1                                                            # This add on the list element since time element increased
        pass


        # Change code above this line *******************************************************************************************************************************


if __name__ == "__main__":
    myLink = LinkedList()
    myLink.add('Mon')
    myLink.add('Tue')
    myLink.add('Wed')
    myLink.add(3)
    myLink.add('Thu')
    myLink.add('Fri')
    myLink.add(1)
    myLink.add('Sat')
    print(f'size = {len(myLink)}')  # size = 8
    print(f'head = {myLink.head()}')  # head = Mon
    myLink.traverse()  # Mon Tue Wed 3 Thu Fri 1 Sat
    myLink.remove('Mon')
    myLink.traverse()  # Tue Wed 3 Thu Fri 1 Sat
    myLink.remove(3)
    myLink.traverse()  # Tue Wed Thu Fri 1 Sat
    myLink.remove('Sat')
    myLink.traverse()  # Tue Wed Thu Fri 1
    myLink.remove('Wed')
    myLink.traverse()  # Tue Thu Fri 1
    print(myLink.remove('Sun'))  # False
    myLink.traverse()  # Tue Thu Fri 1