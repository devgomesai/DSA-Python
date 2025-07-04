class Node:
    def __init__(self,  val):
        self.value = val
        self.next = None
        
def sorted_two_ll(l1, l2):
    arr = []
    
    # for l1
    while l1 is not None:
        arr.append(l1.value)
        l1 = l1.next  
    
    # for l2
    while l2 is not None:
        arr.append(l2.value)
        l2 = l2.next 
        
    arr.sort()
    
    dummy_node = Node(float('-inf'))
    curr = dummy_node
    
    for value in arr:
        curr.next = Node(value)
        curr = curr.next
        
    return dummy_node.next
        
        
def printList(l):
    while l is not None:
        print(l.value, end=" ")
        l = l.next
          
if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(10)
    head1.next.next = Node(15)
    
    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)
    
    
    sorted_head = sorted_two_ll(head1, head2)
    
    printList(sorted_head)