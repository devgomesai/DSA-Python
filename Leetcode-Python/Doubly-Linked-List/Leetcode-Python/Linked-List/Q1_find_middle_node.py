class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        length = 0
        temp = self.head
        # to calculate the length while loop
        while(temp):
            temp = temp.next
            length += 1
        middle_node_index = round(length / 2)
        temp = self.head
        for _ in range(middle_node_index):
            temp = temp.next
        return temp

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

temp = my_linked_list.find_middle_node()
print(temp.value)
