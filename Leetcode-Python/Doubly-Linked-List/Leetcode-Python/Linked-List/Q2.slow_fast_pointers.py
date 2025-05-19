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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        slow = fast = self.head # Create two pointers, slow and fast, both initially pointing to the head of the linked list.

        while fast and fast.next:  #  fast checks for None and fast.next checks for completion
# ***fast.next***:  This ensures that the fast pointer has a next node to move to.
# It specifically prevents errors like accessing fast.next.next when fast.next is None.
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False



















my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True
