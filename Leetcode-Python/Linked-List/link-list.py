class Node:         # Create a Node
    def __init__(self, value):
        self.value = value
        self.next = None    

class LinkedList:
    # Initialization of Linked List 
    def __init__(self, value):
        self.new_node = Node(value) # Create a node with  a value 
        self.head = self.new_node # make the head ponit to the node with a value
        self.tail = self.new_node # also the tail as only one node
        self.length = 1 # as only one node so length is 1
        
    # Append Method
    def Append(self, value): # Only required is the ****tail****
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Display Method
    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Pop Method
    def Pop(self):
        if self.length == 0: # Check if no node
            return None
        else: # if yes node 
            temp = self.head # assign head to a temp pointer
            pre = self.head # assign head to a pre pointer
            while(temp.next): # while true i.e temp.next is not None
                pre = temp
                temp = temp.next
            self.tail = pre # when temp.next is None breaked the loop and make tail as prev node
            self.tail.next = None # and make prev node next as none
            self.length -= 1 # lenght of the list decrement
            if self.length == 0: # if no node in LL
                self.head = None
                self.tail = None
            return temp 
        
    def prepend(self, value): # add node in the begining so ****head****
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


# Create a Linked List with a node creation
print('*' * 13 +'Creating a Linked List'+ '*' * 13)
LinkedList_1 = LinkedList(1)
# Append a Node with a node creation
print('*' * 13 +'Appending in  a Linked List'+ '*' * 13)
LinkedList_1.Append(2)
LinkedList_1.Append(3)
LinkedList_1.Append(4)
LinkedList_1.Append(5)
LinkedList_1.Append(6)
# Display
print('*' * 13 +'Display'+ '*' * 13)
LinkedList_1.Display()
#Pop
print('*' * 13 +'Pop'+ '*' * 13)
poped_element = LinkedList_1.Pop()
# Display
print('*' * 13 +'Display'+ '*' * 13)
LinkedList_1.Display()

print("The Poped Element is :",poped_element.value)

# Add a node in front
node = 10
print(('*' * 13 +'Adding a Node in Front: {}'+ '*' * 13).format(node))
LinkedList_1.prepend(node)

# Display
print('*' * 13 +'Display'+ '*' * 13)
LinkedList_1.Display()