""" HAROLD BERNIE P. GARCIA
   DATALOG : Insertion Sort

   May 8, 2020

   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code.

   Create an insSort(arr, mode) function that employs insertion sort algorithm to sort the elements in the
    array arr. If mode is 0, sort in ascending order otherwise sort in descending order.

<https://www.geeksforgeeks.org/insertion-sort/>

Stay safe everyone!
"""
import operator

    # As long as we haven't reached the beginning and there is an element
    # in our sorted array larger than the one we're trying to insert - move
    # that element to the right

def insSort(arr, mode = 0):
    for B in range (1, len(arr)):
        C = operator.gt if mode else operator.lt
        array_insert = arr[B]
        A = B - 1
        while 0<= A and C(array_insert,arr[A]):
            arr[A+1]= arr[A]
            A -= 1
        arr[A+1] = array_insert
    return arr

    pass

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

    # Insert code above this line

if __name__ == '__main__':
    A = [-3, 64, 1, 25, 12, 59, 22, 26, 11]
    print(insSort(A))
    print(insSort(A, 1))

    B = ['one', 'two', 'too', '19', 'wuhan', 'three', 'covid', 'four', 'five', 'pass']
    print(insSort(B))
    print(insSort(B, 1))