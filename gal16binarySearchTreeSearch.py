""" HAROLD BERNIE P. GARCIA
   DATALOG :  Lab16. Find an element in a Binary Search Tree

   May 13, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.


    Define search(element) method. The method returns True if the element is present in
    the BST otherwise returns False. In binary search trees: each left subtree is less than
    or equal to its parent and each right subtree is greater than or equal to its parent.
    Our tree can only store integer values. If the tree is empty, the method should return False.
"""

class Node:
    def __init__(self, element):
        self._element = element
        self._left = None
        self._right = None

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def getRoot(self):
        return self._root

    def traverse(self, node):
        if node != None:
            self.traverse(node._left)
            print(f'{node._element} ', end="") # No line feed to save screen area
            self.traverse(node._right)

    def add(self, element):
        # Add your code from Lab 13 here  **********************************************************************************************************************

        if self._root is None:                                                                        # Check if the binary tree is Blank then Creates Node.
            self._root = Node(element)                                                                # CREATE the Root of the Node
            self._size += 1                                                                           # element is added linked incresing on length
        else:
            self._add(element, self._root)                                                            #  return if right element is already occupied of binary three
    pass

    def _add(self, element, node_current):
        if element < node_current._element:                                                           # value of the node "<"
            if node_current._left is None:
                node_current._left = Node(element)
                self._size += 1                                                                       # element is added linked incresing on length
            else:
                self._add(element, node_current._left)                                                #  return if right element is already occupied of binary three

        elif element > node_current._element:                                                         # value of the node ">"

            if node_current._right is None:
                node_current._right = Node(element)
                self._size += 1                                                                       # element is added linked incresing on length
            else:
                self._add(element, node_current._right)                                               # return if right element is already occupied of  binary three
    pass

    def search(self, element):
        # Change code below this line **********************************************************************************************************************

        return self._search(self._root, element)

    def _search(self, node_current, element):                                              # If the Linked List is empty, then make the new node as head
        if node_current is None:
            return False                                                                   # FALSE

        if element < node_current._element:                                                # If the Linked List is empty or less than " < "
            return self._search(node_current._left, element)                               # then make the new node as head

        if element == node_current._element:                                               # then make the new node as head
            return True                                                                    # TRUE

        else:
            return self._search(node_current._right, element)                              # return the result "TRUE or FALSE"
        pass

    # Change code above this line **********************************************************************************************************************

if __name__ == "__main__":
    myTree = BinaryTree()
    print(f'search(3): {myTree.search(3)}') # False
    myTree.add(26)
    myTree.add(10)
    myTree.add(31)
    myTree.add(5)
    myTree.add(15)
    myTree.add(28)
    myTree.add(29)
    print(f'length(): {len(myTree)}') # 7

    root = myTree.getRoot()
    print('traverse(): ', end=""); myTree.traverse(root); print("") # 5 10 15 26 29 31

    print(f'search(26): {myTree.search(26)}') # True
    print(f'search(21): {myTree.search(21)}') # False