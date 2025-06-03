class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        node = Node(value)
        self.top = node
        self.height = 1
        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def push(self, value):
        node = Node(value)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top 
            self.top = node
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value
        
    
if __name__ == '__main__':
    st = Stack(10)
    print("height:",st.height)
    st.push(3)
    st.print_stack()
    print("height:",st.height)
    print("Popped Value: ",st.pop())
    st.print_stack()
    print("height:",st.height)
    