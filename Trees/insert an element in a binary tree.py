class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        self.root = self._insert(self.root, element)
    
    def _insert(self, root, element):
        if root is None:
            return TreeNode(element)
        
        if element < root.val:
            root.left = self._insert(root.left, element)
        else:
            root.right = self._insert(root.right, element)
        

        return root
    
################
# the driver method
if __name__ == "__main__":
    tree = BinaryTree()
    keys = [15, 10, 20, 8, 12, 18, 25]
    for key in keys:
        tree.insert(key)
    
    print("Binary tree elements after insertion:")
    # You can perform an in-order traversal to print the elements
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print(node.val, end=" ")
            in_order_traversal(node.right)
    
    in_order_traversal(tree.root)