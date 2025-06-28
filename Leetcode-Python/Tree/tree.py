class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        node = Node(value=value)
        if self.root == None:
            self.root = node
            return True
        temp = self.root
        while(True):
            if node.value == temp.value: # Same node
                return False
            if node.value < temp.value: # left condition
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left 
            else:  # right condition
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right
                
                    
    def contains(self,val):
        temp = self.root
        while temp is not None:
            if val > temp.value: 
                temp = temp.right
            elif val < temp.value:
                temp = temp.left
            else:
                return True
        return False
                    
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

print(tree.contains(27)) # True
print(tree.contains(8)) # False
    
                
                
                    
        
        
        