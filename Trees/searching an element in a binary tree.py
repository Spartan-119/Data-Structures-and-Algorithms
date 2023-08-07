class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
    
    def insert(self, root, value):
        if root is None:
            return TreeNode(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root
    
    def search(self, root, element):
        if root is None or root.value == element:
            return root
        
        if element < root.value:
            return self.seach(root.left, element)
        else:
            return self.search(root.right, element)
        
################
# the driver method
if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]
    root = None

    # the logic for filling the tree
    for key in keys:
        root = TreeNode().insert(root, key)
    
    target = 16
    result = TreeNode().search(root, target)

    if result:
        print(f'Element {target} found!')
    else:
        print(f'Element {target} not found!')