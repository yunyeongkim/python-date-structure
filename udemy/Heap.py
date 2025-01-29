# Heap : Min & Max 
"""
@ log(n)
@ Complete Tree
    1. Fill it from right to left. on each level no gap
@ Duplicates can exist
@ Switching each level is okay.
"""

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    # Helper method
    def _left_child(self,index):
        return 2 * index + 1
    
    def _right_child(self,index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]
    
    def _sink_down(self,index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if (right_index < len(self.heap)) and self.heap[right_index]  > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


        # temp_value = self.heap[index]
        # # temp is not higher than children.
        # def backtracker(start:int):
        #     left_index = self._left_child(start)
        #     right_index = self._right_child(start)
        #     if left_index < len(self.heap) and right_index < len(self.heap):
        #         if temp_value < self.heap[left_index] or temp_value < self.heap[right_index] :
        #             if self.heap[left_index] > self.heap[right_index]:
        #                 self._swap(index , left_index)
        #                 start = left_index
        #             else:
        #                 self._swap(index , right_index)
        #                 start = right_index
        #         else: 
        #             return True
        #         backtracker(start)

        # backtracker(index)
        return True


    # Helper method 

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        # current is index. and 0 means no value.
        while current > 0 and self.heap[current] >  self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)
    
    # remember that it is Heap, remove starts from top. 
    def remove(self):
        if(len(self.heap) == 0):
            return None
        if(len(self.heap) == 1):
            return self.heap.pop()

        # Pointer for max_value
        max_value = self.heap[0]
        # Store last tree node. 
        self.heap[0] = self.heap.pop()
        # sink_down to rerange .
        self._sink_down(0)
        
        return max_value
    




        
my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(50)
my_heap.insert(60)
my_heap.insert(65)

print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)
