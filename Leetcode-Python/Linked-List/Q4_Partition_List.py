class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def partition_list(self, x):
        temp = self.head
        
        nodes_less_than_x = []
        nodes_greater_than_x = []

        # Combine Them
        while temp:
            if temp.value >= x:
                nodes_greater_than_x.append(temp.value)
            else:
                nodes_less_than_x.append(temp.value)
            temp = temp.next

        create_a_dummy_node = Node('inf') # initially making it as the head
        temp = create_a_dummy_node

        for value in nodes_less_than_x:
            temp.next = Node(value=value)
            temp = temp.next

        for value in nodes_greater_than_x:
            temp.next = Node(value=value)
            temp = temp.next
        # after the loop temp points to the last node
        # As temp = create_a_dummy_node copy so as temp changes create_a_dummy_node also changes
        self.head = create_a_dummy_node.next # this is the node after 'inf' 

            

# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Test 1: Normal Case
print("Test 1: Normal Case")
x = 5
print(f"x = {x}")
ll = LinkedList(3)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)
print("Before:", linkedlist_to_list(ll.head))
ll.partition_list(x)
print("After:", linkedlist_to_list(ll.head))
