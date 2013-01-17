# -*- coding: utf-8 -*-
import os

def BinarySearch(arr, val):
    """ Wrapper around the inner function """
    
    def _BinarySearch(start,end,val):
        """
           Naive Binary Search implementation using
           Python's List just as an array

           Prints the Element position and value if found

           Return Bool
        """

        if start>=end:
            print "Not Found"
            return False

        mid=int(round((end-start)/2.0))+start
        print "Midpoint is index : %s" % mid

        if val > arr[mid]:
            _BinarySearch(mid+1,end,val)
        elif val < arr[mid]:
            _BinarySearch(start,mid-1,val)
        else:
            print "found the element : %s at index %s" % (val, mid)
            return True

    return _BinarySearch(0, len(arr)-1, val)

        
        
if __name__ == '__main__':
    arr = [1,5,7,9,11,15,17]
    print arr
    
    print BinarySearch(arr, 15)
    print BinarySearch(arr, 14)
    print BinarySearch(arr, 26)
    print BinarySearch(arr, 5)
    print BinarySearch(arr, 3)
    print BinarySearch(arr, 9)
