class Node:         
    def __init__(self, value):
        self.value = value
        self.next = None    

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def display(self):
        temp = self.head 
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 

    def pop_first_node(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1 

        if self.length == 0:
            self.tail = None
    
        return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first_node()

        if index == self.length - 1:
            return self.pop()

        prev_node = self.get(index - 1)
        rm_node = prev_node.next
        prev_node.next = rm_node.next
        rm_node.next = None
        self.length -= 1
        return rm_node

    def reverse(self):
        temp = self.head  
        self.head = self.tail
        self.tail = temp  

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

LL = None
DONT_END = True
while DONT_END:
    user_input = input(
        """
Welcome to Linked List!!

1. Initialize a Linked List
2. Append 
3. Pop
4. Display 
5. Prepend 
6. Pop First
7. Get
8. Set
9. Insert
10. Exit

Enter Choice: """
    )
    
    if user_input == '1':
        number = int(input("Initialize a linked List with the starting Value: "))
        LL = LinkedList(number)
        print(f'Linked List: Initialized with {number}')
    
    elif user_input == '2':
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            user = int(input("Enter a Value to Append in the Linked List: "))
            LL.append(user)
            print("Value Appended Successfully!")
    
    elif user_input == '3':
        if LL is None or LL.length == 0:
            print("Error: No elements to pop!")
        else:
            popped_node = LL.pop()
            print(f"\n** Popped Value: {popped_node.value} **")
    
    elif user_input == "4":
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            LL.display()
    
    elif user_input == "5":
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            user = int(input("Enter a Value to Prepend in the Linked List: "))
            LL.prepend(user)
    
    elif user_input == "6":
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            LL.pop_first_node()
            print("Success Popping the First Node!!")
    
    elif user_input == "7":
        if LL is None:
            print("Error: Create a Linked List first!") 
        else:
            index = int(input("Enter an index to get: "))
            node = LL.get(index)
            if node is None:
                print("Invalid Index!")
            else:
                print(f"Value at index {index}: {node.value}")
    
    elif user_input == '8':
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            index, value = map(int, input("Enter the Index and Value (separated by space): ").split())
            if LL.set(index, value):
                print("Node is Updated")
            else:
                print('Error Updating the Node')
    
    elif user_input == '9':
        if LL is None:
            print("Error: Create a Linked List first!")
        else:
            index, value = map(int, input("Enter the Index and Value to Insert the Node (separated by space): ").split())
            if LL.insert_node(index, value):
                print("Node is inserted")
            else:
                print('Error Inserting the Node')
    
    elif user_input == "10":
        print("Exiting the Program.....")
        DONT_END = False
    
    else:
        print("Invalid Choice! Please enter a valid option.")
