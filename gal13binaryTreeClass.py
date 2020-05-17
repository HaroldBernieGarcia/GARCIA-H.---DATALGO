""" HAROLD BERNIE P. GARCIA
   DATALOG :  Add a New Element to a Binary Search Tree

   May 13, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.

    Defined is a skeleton of a binary search tree structure with a method to create nodes for the tree. Each node may
    have a left and right value. These will be assigned child subtrees if they exist. In the binary search tree, create
    a method to add new values to the binary search tree. The method should be called add and it should accept an integer
    value to add to the tree. Take care to maintain the invariant of a binary search tree: the value in each left child
    should be less than or equal to the parent value, and the value in each right child should be greater than or equal to
    the parent value. The tree cannot hold duplicate values.

    The tree's length should increase by one every time an element is added to the tree.

    Hint: trees are naturally recursive data structures!

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

    # Change code below this line *************************************************************************************************************************

    def add(self, element):
        if self._root is None:                                                       # If the Linked List is empty, then make the new node as head
            self._root = Node(element)                                               # Create a new node, Put in the data,Set next as None
            self._size += 1                                                          # element is added to the linked incresing
        else:
            self._add(element, self._root)                                           # if a element has been occupied

    pass

    def _add(self, element, node_current):
        if element < node_current._element:

            if node_current._left is None:                                           # if the value in left is "blank"

                self._size += 1                                                      # element is added to the linked incresing
                node_current._left = Node(element)                                   # sets the value left node into the new node

            else:

                self._add(element, node_current._left)

        elif element > node_current._element:
            if node_current._right is None:                                          # If the Linked List is empty or grater than " > "
                self._size += 1                                                      # element is added linked incresing on length
                node_current._right = Node(element)

            else:
                self._add(element, node_current._right)

    # Change code above this line *************************************************************************************************************************


if __name__ == "__main__":
    myTree = BinaryTree()
    myTree.add(26)
    myTree.add(10)
    myTree.add(31)
    myTree.add(5)
    myTree.add(15)
    myTree.add(28)
    print(f'len(): {len(myTree)}') # 6
    myTree.add(29)
    print(f'len(): {len(myTree)}') # 7
    myTree.add(10) # Duplicate
    print(f'len(): {len(myTree)}') # 7

    root = myTree.getRoot()
    print('traverse(): ', end=""); myTree.traverse(root); print("") # 5 10 15 26 28 29 31