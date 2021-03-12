# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:04:21 2021

@author: abin.varghese01
"""

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

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
   4    5     6     7 
'''

root_node.left.left = BinaryTreeNode(4)
root_node.left.right = BinaryTreeNode(5)
root_node.right.left = BinaryTreeNode(6)
root_node.right.right = BinaryTreeNode(7)

# InOrder Traversal

'''
in InOrder Traversal the root is visited between the subtrees
1. Traverse the left subtree
2. Visit the root
3. Traverse the right subtree
'''

# Recursive approach
def InOrder_recursive(root, result):
    if root is None:
        return
    else:
        InOrder_recursive(root.left, result)
        result.append(root.data)
        InOrder_recursive(root.right, result)
        return result
        
print("Recursive method: ",InOrder_recursive(root_node, []))

# Iterative approach
def InOrder_iterative(root, result):
    if root is None:
        return
    else:
        stack = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result
                
print("Iterative method: ", InOrder_iterative(root_node, []))