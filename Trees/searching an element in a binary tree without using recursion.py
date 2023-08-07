class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, element):
        self.root = self._insert(self.root, element)
    
    def _insert(self, root, element):
        if root is None:
            return TreeNode(element)

        if element < root.value:
            root.left = self._insert(root.left, element)
        else:
            root.right = self._insert(root.right, element)
        
        return root
    
    def search(self, target):
        return self._search(self.root, target)
    
    def _search(self, root, target):
        if root is None or root.value == target:
            return root
        
        stack = []
        current = root

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            
            else:
                current = stack.pop()
                if current.value == target:
                    return current
                current = current.right

        return None

################
# the driver method
if __name__ == "__main__":
    tree = BinaryTree()
    keys = [15, 10, 20, 8, 12, 18, 25]
    for key in keys:
        tree.insert(key)
    
    target = 12
    result = tree.search(target)
    
    if result:
        print(f"Element {target} found in the binary tree.")
    else:
        print(f"Element {target} not found in the binary tree.")