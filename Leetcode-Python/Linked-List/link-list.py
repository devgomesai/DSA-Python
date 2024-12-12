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

    # Insert a Node at a particular index
    def insert_node(self, index, value):

        if index < 0 or index > self.length:
            return False # index is out of range

        if index == 0: # Start
            return self.prepend(value=value)

        if index == self.length: # End
            return self.Append(value=value)
        
        # Middle
        node = Node(value=value)
        temp = self.get(index=index-1) # node before main index i.e if index = 2 then prev_node is node at 1
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True
        
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
    def Pop(self): # two pointers temp and pres
        if self.length == 0: # Check if no node
            return None
        else: # if yes there is a node 
            temp = self.head # assign head to a temp pointer
            pre = self.head # assign head to a pre pointer
            while(temp.next): # while true i.e temp.next is not None
                pre = temp
                temp = temp.next
            self.tail = pre # when temp.next is None breaked the loop and make tail as prev node
            self.tail.next = None # and make prev node next as none
            self.length -= 1 # lenght of the list decrement
            if self.length == 0: # if no node in LL  ****self.length -= 1****
                self.head = None
                self.tail = None
            return temp 

    # Pop First Node
    def pop_first_node(self):
        if self.length == 0:
            return None

        temp = self.head # temp varaible to be th start of LL
        self.head = self.head.next # make the head as the 2nd node or next node 
        temp.next = None # break the link of temp i.e the first node
        self.length -= 1 

        if self.length == 0: # if no node in LL this is for ****self.length -= 1**** when turns to zero
            # self.head = None not required as happens on line 77
            self.tail = None
    
        return temp
        
    # Add Node to the Begining
    def prepend(self, value): # add node in the begining so ****head****
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # self.head is the pointer to the start of LL node so giving the head pointer to the new node
            self.head = new_node # updating the head with the new node
        self.length += 1

    # get a node via index
    def get(self, index):
        # Check if the given index is valid
        if index < 0 or index >= self.length:
            return None
        # assign head to temp
        temp = self.head
        # for loop to move in the LL and get to the index node
        for _ in range(index):
            temp = temp.next
        return temp # once reached the node return it

    # Set a node value at a given index
    def set(self, index, value):
        # call get() method to get the node
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    # remove a node
    def remove(self, index):

        if index < 0 or index >=self.length:
            return None

        if index == 0:
            return self.pop_first_node()

        if index == self.length - 1:
            return self.Pop()
        # middle node
        prev_node = self.get(index=index-1)
        rm_node = prev_node.next
        prev_node.next = rm_node.next
        rm_node.next = None
        self.length -= 1
        return rm_node

    # Reverse a Linked List (********)
    def reverse(self):

        temp = self.head  # set temp with head

        self.head = self.tail # set head with tail
        self.tail = temp  # set tail with head but you keep the copy of head in temp

        after = temp.next # create 2 variables
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
