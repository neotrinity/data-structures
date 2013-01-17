# -*- coding: utf-8 -*-

def bubble_sort(li):
    """ In-Place Bubble Sort """
    def bubble(li,length):
        if length <= 0:
            return li
        for i in xrange(length):
            if li[i+1]<li[i]:
                tmp=li[i]
                li[i]=li[i+1]
                li[i+1]=tmp
        bubble(li,length-1)
    bubble(li,len(li)-1)
    
def selection_sort(li):
    """ In-Place Selection Sort """
    end = len(li)
    def find_min_index(li,start,end):
        min_index=start
        for i in xrange(start,end):
            if li[i]<li[min_index]:
                min_index=i
        return min_index
    for i in xrange(end):
        min_index=find_min_index(li,i,end)
        tmp=li[i]
        li[i]=li[min_index]
        li[min_index]=tmp
	
	
def insertion_sort(li):
    """ In-Place Insertion Sort """
    end=len(li)
    for i in xrange(end):
        temp = li[i]
        mark=i
        for j in xrange(i,0,-1):
            if li[j-1]>temp:
                li[j]=li[j-1]
                mark-=1
            else:
                break
        if mark != i:
            li[mark]=temp
		

def merge(left,right):
    """ Merges 2 (sorted) Lists
        This is used as a helper in merge sort
    """
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            del left[0]
        else:
            merged.append(right[0])
            del right[0]
	    
    merged.extend(left)
    merged.extend(right)
	
    return merged
    
def mergesort(list):
    """ Merge Sorts a list and
        returns a copy of the new sorted list
    """
    
    if len(list) <= 1:
        return list
    
    mid = len(list)/2
    
    left = list[:mid]
    right = list[mid:]
    
    sortedLeft = mergesort(left)
    sortedRight = mergesort(right)
    
    return merge(sortedLeft,sortedRight)

if __name__ == '__main__':

    li = [4,5,2,1,7,8,6]

    print "unsorted : ", li
    bubble_sort(li)
    print "bubble sorted : ", li

    li = [4,5,2,1,7,8,6]

    print "unsorted : ", li
    selection_sort(li)
    print "selection sorted : ", li


    li = [4,5,2,1,7,8,6]

    print "unsorted : ", li
    insertion_sort(li)
    print "insertion sorted : ", li

    li = [4,5,2,1,7,8,6]

    print "unsorted : ", li
    mslist = mergesort(li)
    print "merge sorted : ", mslist
