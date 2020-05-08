""" HAROLD BERNIE P. GARCIA
   DATALOG : Selection Sort

   May 8, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.

   Create a selSort(arr, mode) function that employs selection sort algorithm to sort the elements in the
      array arr. If mode is 0, sort in ascending order otherwise sort in descending order.

<https://www.geeksforgeeks.org/selection-sort/>

Stay safe everyone!
"""

def selSort(arr, mode = 0):

    # Insert code below this line

    # As long as we haven't reached the beginning and there is an element
    # in our sorted array larger than the one we're trying to insert - move
    # that element to the right

    if len(arr) <= 1:
        return arr
    for x in range(len(arr)):
        temp_index = x
        for y in range(x+1, len(arr)):
            if mode and arr[y] > arr[temp_index] or not mode and arr[y] < arr[temp_index]:
                temp_index= y
        arr[x], arr[temp_index] = arr[temp_index], arr[x]
    return arr

    for fillslot in range(len(A) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if A[location] > A[positionOfMax]:
                positionOfMax = location

        temp = A[fillslot]
        A[fillslot] = A[positionOfMax]
        A[positionOfMax] = temp

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at fillslot

    pass


    # Insert code above this line


if __name__ == '__main__':
    A = [-3, 64, 1, 25, 12, 59, 22, 26, 11]
    print(selSort(A))
    print(selSort(A, 1))

    B = ['one', 'two', 'too', '19', 'wuhan', 'three', 'covid', 'four', 'five', 'pass']
    print(selSort(B))
    print(selSort(B, 1))