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
            if node.value < temp.value: # left conditio
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
                    
                
                
                
                    
        
        
        