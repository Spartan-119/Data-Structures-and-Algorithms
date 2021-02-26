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

#root_node.left.left = BinaryTreeNode(4)

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''

root_node.left.left = BinaryTreeNode(4)
root_node.left.right = BinaryTreeNode(5)
root_node.right.left = BinaryTreeNode(6)
root_node.right.right = BinaryTreeNode(5)

# pre-order traversal
''' in preorder traversal, each node is processed
before (pre) either of its subtrees.

To move to the right subtree after processing the left
subtree, we must maintain the root information.
Thus, Stacks are preferred due to their LIFO property.
Due to the LIFO structure, it's possible to get the information 
about the right subtrees back in the reverse order.

1. Visit the root
2. Traverse the left subtree in Preorder
3. Traverse the right subtree in Preorder'''

# the nodes of the tree would be visited in the order: 1 2 4 5 3 6 7

# PREORDER RECURSIVE TRAVEL
def preorder_recursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorder_recursive(root.left, result)
    preorder_recursive(root.right, result)

# PREORDER NON RECURSIVE TRAVEL
def preorder_iterative(root, result):
    if not root:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        result.append(node.data)
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)