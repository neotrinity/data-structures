
class Node(object):
    def __init__(self,obj):
        self._val=obj
        self._next=None
        self._prev=None
        
        
class DLinkedList(object):
    """ Doubly Linked List Implementation """
    def __init__(self):
        self._right=None
        self._left=None
        self._length=0
        
    def add_right(self,obj):
        """ Add the payload to the right end of the List """
        node=Node(obj)
        if not self._right and not self._left:
            self._right=node
            self._left=node
        else:
            self._right._next=node
            node._prev=self._right
            self._right=node
        self._length+=1
            
    def add_left(self,obj):
        """ Add the payload to the left end of the List """
        node=Node(obj)
        if not self._right and not self._left:
            self._right=node
            self._left=node
        else:
            self._left._prev=node
            node._next=self._left
            self._left=node
        self._length+=1
        
    def print_l_to_r(self):
        """ Print the elements from left-to-right """
        node=self._left
        while node:
            print node._val
            node=node._next
        
    def print_r_to_l(self):
        """ Print the elements from right-to-left """
        node=self._right
        while node:
            print node._val
            node=node._prev
    def pop_right(self):
        """ Pop the leftmost element """
        if self._right:
            node=self._right
            if node._prev:
                self._right=node._prev
                self._right._next=None
                self._length-=1
            else:
                self._left=self._right=None
            return node
        else:
            print "Empty !"
            
    def pop_left(self):
        """ Pop the rightmost element """
        if self._left:
            node=self._left
            if node._next:
                self._left=node._next
                self._left._prev=None
                self._length-=1
            else:
                self._left=self._right=None
            return node
        else:
            print "Empty !"      

    def insert_at(self, index, obj):
        pass

    def delete(self, obj):
        pass
