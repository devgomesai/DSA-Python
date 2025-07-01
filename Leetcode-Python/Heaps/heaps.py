# ---------
# Max Heap
# ---------
#           (100)
#         /      \
#      (99)       (75)
#     /   \       /  \ 
#  (58)   (72)  (61) (18)
#--------------------------------------------------------------
#  0  1  2  3  4  5  6  => index
# 100 99 75 58 72 61 18  => node values
# For arr index that starts from 0 index
# left_child_idx = 2 * parent_index + 1
# right_child_idx = 2 * parent_index + 2

# ------------------------------------------------------------------------------------------------------------------     
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self,index):
        return 2 * index + 1

    def _right_child(self,index):
        return 2 * index + 2 
    
    def _parent(self, index):
        return (index-1) // 2 
    
    def _swap(self,index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, value):
        # append the value in arr
        self.heap.append(value)
        # get the index of the appended value from the arr i.e the current pointer
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))                
            current = self._parent(current)
            
    def get_right_child(self, value):
        try:
            _index = self.heap.index(value)
            _right_index = self._right_child(_index)
            if _right_index < len(self.heap):
                print(f"Right Child of {value}: {self.heap[_right_index]}")
        except ValueError:
            print(f"Value {value} not found in heap.")
        
    def get_left_child(self,value):
        try:
            _index = self.heap.index(value)
            _left_index = self._left_child(_index)
            if _left_index < len(self.heap):
                print(f"Left Child of {value}: {self.heap[_left_index]}")
        except ValueError:
            print(f"Value {value} not found in heap.")
    
    
    
max_heap = MaxHeap()
max_heap.insert(99)
max_heap.insert(72)
max_heap.insert(61)
max_heap.insert(58)

print(max_heap.heap)

max_heap.insert(100)
print('-'*16)
print(max_heap.heap)
print('-'*16)
max_heap.insert(75)
print(max_heap.heap)

max_heap.get_right_child(100)
max_heap.get_left_child(100)

                
