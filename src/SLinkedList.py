# -*- coding: utf-8 -*-
import os

class Node(object):
  def __init__(self,obj):
    self.data=obj
    self.next=None
    
class SLinkedList(object):
  def __init__(self):
    self.head=None
    self.tail=None
    self.length=0
  
  def add_last(self,obj):
    if self.length == 0:
      self.head = self.tail = Node(obj)
    else:
      n=Node(obj)
      self.tail.next = n
      self.tail = n
    self.length+=1
    
  def add_first(self,obj):
    if self.length == 0:
      self.head = self.tail = Node(obj)
    else:
      n=Node(obj)
      n.next=self.head
      self.head=n
      self.length+=1    
    
  def add_at(self,index,obj):
    if self.length == 0:
      return None
    elif index > self.length:
      print " Index Error "
    elif index == 0:
      self.add_first(obj)
    elif index == self.length:
      self.add_last(obj)
    else:
      prev=self.head
      cur=self.head.next
      i=1
      while (i<=self.length-1):
	if i==index:
	  n=Node(obj)
	  prev.next=n
	  n.next=cur
	  self.length+=1
	  break
	else:
	  prev=cur
	  cur=cur.next
	i+=1
    
  def delete_first(self):
    if self.length == 0:
      print " Empty "
    else:
      n=self.head
      self.head=self.head.next
      del n
      self.length-=1
      
  def print_l_r(self):
    if self.length == 0:
      return None
    else:
      n=self.head
      while n:
	print n.data
	n=n.next
  
  def delete_at(self,index):
    if self.length == 0:
      return None
    elif index > self.length:
      print " Index Error "
    elif index == 0:
      self.delete_first()
    else:
      #nodes=self.iternateNode()
      prev=self.head
      cur=self.head.next
      i=1
      while (i<=self.length-1):
	if i==index:
	  prev.next=cur.next
	  del cur
	  if i == self.length-1:
	    self.tail=prev
	  self.length-=1
	  break
	else:
	  prev=cur
	  cur=cur.next
	i+=1
    
