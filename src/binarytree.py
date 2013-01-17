# -*- coding: utf-8 -*-
import os


class TreeNode(object):
    def __init__(self,key,value=None):
	self.key=key
	self.data=value
	self.leftChild=None
	self.rightChild=None
	
    def __repr__(self):
	return " Key : %s Value : %s " % (self.key, self.data)
	
	
class BinaryTree(object):
    """
         Binary Tree Implementation
    """

    def __init__(self):
	self.root=None
	
    def insert(self,key,value):
	if self.root == None:
	    self.root = TreeNode(key,value)
	else:
	    node = self.root
	    while (node != None):
		if (key < node.key):
		    if node.leftChild == None:
			node.leftChild = TreeNode(key,value)
			node = None
		    else:
		        node = node.leftChild
		elif (key >= node.key):
		    if node.rightChild == None:
			node.rightChild = TreeNode(key,value)
			node = None
		    else:
		        node = node.rightChild
		        
    def find(self,key):
	node = self.root
	while (node != None):
	    if (key < node.key):
		node = node.leftChild
	    elif (key > node.key):
		node = node.rightChild
	    else:
		return node		
	
    def _link(self,child):
	node = self.root
	while (node != None):
	    if (child.key < node.key):
		if node.leftChild == None:
		    node.leftChild = child
		    return
		else:
		    node = node.leftChild
	    elif (child.key >= node.key):
		if node.rightChild == None:
		    node.rightChild = child
		    return
		else:
		    node = node.rightChild
		    
    def delete(self,key):
	node = self.find(key)
	if node:
	    rc = node.rightChild
	    lc = node.leftChild
	    del node
	    if rc:
		self._link(rc)
	    if lc:
		self._link(lc)
		
    def _inorder(self,node):   
	if node.leftChild:
	    self._inorder(node.leftChild)
	node.showNode()
	if node.rightChild:
	    self._inorder(node.rightChild)
	    
    def inorder(self):
	node=self.root
	self._inorder(node)


if __name__ == '__main__':	
    bt = BinaryTree()
    bt.insert(50,'50')
    bt.insert(40,'40')
    bt.insert(30,'30')
    bt.insert(45,'45')
    bt.insert(20,'20')
    bt.insert(35,'35')
    bt.insert(42,'42')
    bt.insert(47,'47')

    bt.delete(40)

    print bt.root.leftChild
    print bt.root.leftChild.leftChild


	    
