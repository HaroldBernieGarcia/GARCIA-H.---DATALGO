""" HAROLD BERNIE P. GARCIA
   DATALOG :   Create a Linked List Search

   May 11, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.


    Write an isEmpty method that checks if the linked list is empty, an indexOf method that returns the index of a given element, and
    an elementAt that returns an element at a given index.

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

    # include your add method here *************************************************************************************************************************************

    def add(self, element):
        # Change code below this line

        Set = Node(element)                                         # Create a new node, Put in the data,Set next as None
        if self._head is None:                                      # If the Linked List is empty, then make the new node as head
            self._head = Set                                        # new Linked List
            self._size += 1                                         # element is added to the linked incresing

            return
        Data = self._head
        while Data._next:
            Data = Data._next
        Data._next = Set
        self._size += 1

        pass

    # Change code below this line **********************************************************************************************************************************************

    def indexOf(self, element):
        current = self._head
        search_element = element
        found = False
        count = 0


        while current != None and not found:
            if current._element == search_element:
                found = True
                return count
            else:
                current = current._next
                count += 1
        if current == None and found == False:
            return -1


    def isEmpty(self):
        pass
    pass


    def elementAt(self, at):
        current = self._head
        count = 0
        while current:
            if count == at:
                return current._element
            count += 1
            current = current._next
        return None

    pass
    # Change code above this line***************************************************************************************************************************************


if __name__ == "__main__":

    myLink = LinkedList()

    print(myLink.isEmpty())  # True

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

    print(myLink.isEmpty())  # False

    print(myLink.indexOf('Mon'))  # 0
    print(myLink.indexOf('Sat'))  # 7
    print(myLink.indexOf('Sun'))  # -1

    print(myLink.elementAt(0))  # Mon
    print(myLink.elementAt(1))  # Tue
    print(myLink.elementAt(6))  # 1
    print(myLink.elementAt(-1))  # None
    print(myLink.elementAt(8))  # None