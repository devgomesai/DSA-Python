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
            
    def _sink_down(self, index):
        max_index = index # get the head index i.e 0
        while True:
            left_index = self._left_child(index=index)
            right_index = self._right_child(index=index)
            
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
                
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
                
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
        
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0] # store first item into max_value variable
        self.heap[0] = self.heap.pop() # set the index 0 to the last value of the heap  
        self._sink_down(0) # sink the top value based on prev code to sort the max-heap
        
        return max_value
            
    # def get_right_child(self, value):
    #     try:
    #         _index = self.heap.index(value)
    #         _right_index = self._right_child(_index)
    #         if _right_index < len(self.heap):
    #             print(f"Right Child of {value}: {self.heap[_right_index]}")
    #     except ValueError:
    #         print(f"Value {value} not found in heap.")
        
    # def get_left_child(self,value):
    #     try:
    #         _index = self.heap.index(value)
    #         _left_index = self._left_child(_index)
    #         if _left_index < len(self.heap):
    #             print(f"Left Child of {value}: {self.heap[_left_index]}")
    #     except ValueError:
    #         print(f"Value {value} not found in heap.")
    
    
    
max_heap = MaxHeap()
max_heap.insert(95)
max_heap.insert(75)
max_heap.insert(80)
max_heap.insert(55)
max_heap.insert(60)
max_heap.insert(50)
max_heap.insert(65)

print(max_heap.heap)

max_heap.remove()

print(max_heap.heap)
