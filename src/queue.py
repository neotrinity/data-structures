class Queue(object):
    """ Naive queue implementation using python list
        TODO :  Replace python list with LinkedLists
    """
    def __init__(self,maxsize=100):
        self._items=0
        self._li=[]
        self._first=None
        
    def enqueue(self,obj):
        self._li.insert(self._items,obj) 
        self._items+=1
        
    def dequeue(self):
        ret=self._li[0]
        del self._li[0]
        self._items-=1
        return ret
