class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: # enqueue from end : dequeue from start FIFO (Queue)
    def __init__(self, value):
        node = Node(value)
        self.start = node
        self.end = node
        self.length = 1
    
    def print_queue(self):
        temp = self.start
        while temp != None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value): 
        node = Node(value)
        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
        self.length += 1
        
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.start
        if self.length == 1:
            self.start = None
            self.end = None 
        else:
            self.start = self.start.next
            temp.next = None
        self.length -= 1
        return temp


        
        
queue = Queue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.print_queue()
queue.dequeue()
print('*'*3)
queue.print_queue()