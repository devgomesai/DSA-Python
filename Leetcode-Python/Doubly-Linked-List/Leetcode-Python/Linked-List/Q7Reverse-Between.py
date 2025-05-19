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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def get_node(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def reverse_between(self, start_index, end_index):
        if start_index == end_index:
            return

        prev = None
        current = self.head

        for _ in range(start_index):
            prev = current
            current = current.next

        last_node_of_first_part = prev
        last_node_of_sublist = current
        next_node = None

        for _ in range(end_index - start_index + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            self.head = prev

        last_node_of_sublist.next = current

        return 'Done'

# Testing the updated code
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()
