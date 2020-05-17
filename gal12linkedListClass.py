""" HAROLD BERNIE P. GARCIA
   DATALOG :   Create a Linked List Class

   May 11, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.


    Write an add method that assigns the first node you push to the linked list to the head; after that,
    whenever adding a node, every node should be referenced by the previous node's next property.

    Note
    Your list's length should increase by one every time an element is added to the linked list.

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

    # Change code below this line *******************************************************************************************

    def add(self, element):                                         # This function is in LinkedList class
                                                                    # Function to insert a new node at the beginning

        Set = Node(element)                                       # Create a new node, Put in the data,Set next as None

        if self._head is None:                                    # If the Linked List is empty, then make the new node as head
            self._size += 1
            self._head = Set

            return

        Data = self._head                                         # Else traverse till the last node
        if Data._next:

            Data = Data._next                                     # Change the next of last node

        self._size += 1
        Data._next = Set

        pass

        # Change code above this line *********************************************************************************************


if __name__ == "__main__":
    myLink = LinkedList()
    myLink.add('Mon')
    myLink.add('Tue')
    myLink.add('Wed')
    #myLink.add('Thru')
    #myLink.add('Fri')
    print(len(myLink))
    print(myLink.head())
    myLink.traverse()