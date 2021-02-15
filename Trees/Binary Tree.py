# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:09:26 2021

@author: Abin
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# creating nodes now

# root node
root_node = BinaryTreeNode(1)

'''
  root_node
 /         \
None      None
'''

root_node.left = BinaryTreeNode(2)
root_node.right = BinaryTreeNode(3)

'''
              1
           /    \
         2        3
       / \       / \
    None None None None
'''

root_node.left.left = BinaryTreeNode(4)

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''