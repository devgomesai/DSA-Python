class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll(self):
        temp = self.head
        if self.head is None:
            print("DLL is Empty")
            return
        print("** Display **")
        while temp is not None:
            print(f"|{temp.value}|", end=" <-> ")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # link 1 ->
            self.head.prev = new_node  # link 2 <-
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:  # Base Case
            return None
        temp = self.head
        if index < self.length / 2:  # First Half => head side
            for _ in range(index):
                temp = temp.next
        else:  # Second Half => tail side :=> to make the code more efficient
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp.value

    def set_value(self, index, value):
        temp = self.get(index=index)
        if temp:
            temp.value = value
            return True
        return False

# Interactive Menu
DLL = None
DONT_END = True
while DONT_END:
    user_input = input(
        """
Welcome to Doubly Linked List!!

1. Initialize a DLL
2. Append 
3. Pop
4. Display 
5. Prepend 
6. Pop First
7. Get
8. Set
9. Exit

Enter Choice: """
    )

    if user_input == "1":
        user = int(input("Enter a Value to Start the Doubly Linked List: "))
        DLL = DoublyLinkedList(user)
        print("Doubly Linked List Created Successfully!")

    elif user_input == "2":
        if DLL is None:
            print("Error: Create a DLL first!")
        else:
            user = int(input("Enter a Value to Append in the Doubly Linked List: "))
            DLL.append(user)

    elif user_input == "3":
        if DLL is None or DLL.length == 0:
            print("Error: No elements to pop!")
        else:
            popped_node = DLL.pop()
            print(f"\n** Popped Value: {popped_node.value} **")

    elif user_input == "4":
        if DLL is None:
            print("Error: Create a DLL first!")
        else:
            DLL.print_dll()

    elif user_input == "5":
        if DLL is None:
            print("Error: Create a DLL first!")
        else:
            user = int(input("Enter a Value to Prepend in the Doubly Linked List: "))
            DLL.prepend(user)

    elif user_input == "6":
        if DLL is None:
            print("Error: Create a DLL first!")
        else:
            DLL.pop_first()
            print("Success Poping the First Node!!")

    elif user_input == "7":
        if DLL is None:
            print("Error: Create a DLL first!") 
        else:
            index = int(input("Enter an index to get: "))
            value = DLL.get(index)
            if value is None:
                print("Invalid Index!")
            else:
                print(f"Value at index {index}: {value}")

    elif user_input == '8':
        if DLL is None:
            print("Error: Create a DLL first!")
        else:
            index, value = input("Enter the Index and Value (separated by space): ").split()
            index = int(index)
            node_updated = DLL.set_value(index, value)
            if node_updated:
                print("Node is Updated")
            else:
                print('Error Updating the Node')

    elif user_input == "9":
        print("Exiting the Program.....")
        DONT_END = False

    else:
        print("Invalid Choice! Please enter a valid option.")
