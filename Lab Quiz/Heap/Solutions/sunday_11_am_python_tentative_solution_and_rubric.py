# -*- coding: utf-8 -*-
"""Sunday_11 am_Python Tentative Solution and Rubric.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WsQ-SEpLVXXNGJRJDxN0dB-L-7mnzamK

## **Set A**
"""

class MinHeap:
    '''Students just have to write these tree functions'''
    def extract_min(self):
        if self.__heapSize == 0:
            raise Exception("Heap underflow")
        min_value = self.__arr[1]
        self.__arr[1] = self.__arr[self.__heapSize]
        self.__arr[self.__heapSize]  = 0
        self.__heapSize -= 1
        self.__sink(1)
        return min_value

    def __sink(self, index):
        while 2 * index <= self.__heapSize:
            child = 2 * index
            if child < self.__heapSize and self.__arr[child] > self.__arr[child + 1]:
                child += 1
            if self.__arr[index] <= self.__arr[child]:
                break
            self.__arr[index], self.__arr[child] = self.__arr[child], self.__arr[index]
            index = child

    def minOperation(self):
      operations = 0
      while self.__heapSize > 0:
          min_val = self.extract_min()
          original_size = self.__heapSize
          i = 1
          while i < original_size+1:
              self.__arr[i] -= min_val
              i+=1
          operations += 1
      return operations

# In the sink function, accurate child index calculation and comparison  = 3
# In the sink function, proper swapping mechanism and loop termination  = 3
# Heap emptiness check = 1
# Heap reorganization = 2
# Correct loop structure and termination = 2
# Correct Calculation (subtraction for set A and floor division conditions for set B ) = 3
# Correct Output return = 1

"""## Set B"""

def minOperation(self):
  '''Performs the min operation: repeatedly extracts the minimum value and
floor divides all remaining values by the extracted minimum value
until either all values become zero or the heap is empty. Returns the number of operations performed.'''
  operations = 0
  while self.__heapSize > 0:
      min_val = self.extract_min()
      original_size = self.__heapSize

      # Subtract min_val from each remaining value and reinsert if non-zero
      i = 1
      while i < original_size+1:
          self.__arr[i] = self.__arr[i] // min_val
          i+=1
      operations += 1
  return operations



# The extractMin() and sink() function will be same like set A

# In the sink function, accurate child index calculation and comparison  = 3
# In the sink function, proper swapping mechanism and loop termination  = 3
# Heap emptiness check = 1
# Heap reorganization = 2
# Correct loop structure and termination = 2
# Correct Calculation (subtraction for set A and floor division conditions for set B ) = 3
# Correct Output return = 1

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.heap = [0] * capacity

    def insert(self, value):
        if self.size == self.capacity:
            raise OverflowError("Heap is full")

        self.heap[self.size] = value
        self.size += 1
        self.swim(self.size - 1)

    def extractMin(self):
      temp = self.heap[1]
      self.heap[1] = self.heap[self.size]
      self.heap[self.size] = 0
      self.size -= 1
      self.sink(1)
      return temp

    def buildHeap(self, arr):
        self.size = len(arr)
        self.heap = [0] + arr
        return root

    def sort(self):
        original_size = self.size
        for i in range(original_size - 1, -1, -1):
            self.heap[i] = self.extractMin()
        self.size = original_size  # Reset size for further operations
        return self.heap[:original_size]

    def swim(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def sink(self, index):
      left_index = 2 * index
      right_index = 2 * index + 1
      if left_index > self.size:
        return
      if left_index == self.size:
        if self.heap[index] < self.heap[left_index] and self.heap[left_index] != 0:
          temp = self.heap[index]
          self.heap[index] = self.heap[left_index]
          self.heap[left_index] = temp
        return
      if self.heap[left_index] != 0 and self.heap[right_index] != 0:
        if self.heap[index] < self.heap[left_index] and self.heap[left_index] < self.heap[right_index]:
          return
        if self.heap[left_index] < self.heap[right_index]:
          temp = self.heap[index]
          self.heap[index] = self.heap[left_index]
          temp = self.heap[index]
          self.heap[index] = self.heap[left_index]
          self.heap[left_index] = temp
          self.sink(left_index)
        else:
          temp = self.heap[index]
          self.heap[index] = self.heap[right_index]
          self.heap[right_index] = temp
          self.sink(right_index)


    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def min_op_find(self):
      count = 0
      q = self.size
      for i in range(q):
        x = self.extract_min()
        for j in range(self.size):
          self.heap[j] = self.heap[j] // x
        count += 1
      return count

if __name__ == "__main__":
    # Initialize the array
    arr = [2, 100, 100]

    # Create a MinHeap with capacity equal to the size of the array
    min_heap = MinHeap(len(arr))

    # Build the heap with the array elements
    for value in arr:
        min_heap.insert(value)

    # Perform the custom min operation and count operations
    count = min_heap.min_op_find()
    print("Custom operation count:", count)

