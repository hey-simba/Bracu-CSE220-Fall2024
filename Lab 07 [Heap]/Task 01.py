
import numpy as np

class MinHeap:
    def __init__(self, initial_capacity=10):
        self.heap = np.empty(initial_capacity + 1, dtype=object)
        self.size = 0
        self.capacity = initial_capacity

    def insert(self, value):
        self.size += 1
        if self.size > self.capacity:
            self.resize()
        self.heap[self.size] = value
        self.swim(self.size)

    def resize(self):
        self.capacity *= 2
        self.heap = np.resize(self.heap, self.capacity + 1)

    def swim(self, k):
        while k > 1 and self.heap[k // 2] > self.heap[k]:
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def extractMin(self):
        if self.size == 0:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self.sink(1)
        return min_val

    def sink(self, k):
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self.heap[j] > self.heap[j + 1]:
                j += 1
            if self.heap[k] <= self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def sort(self):
        sorted_array = []
        original_size = self.size
        while self.size > 0:
            sorted_array.append(self.extractMin())
        self.size = original_size
        return sorted_array

# Example usage:
heap = MinHeap()
heap.insert(4)
heap.insert(1)
heap.insert(3)
heap.insert(2)
heap.insert(16)
heap.insert(9)
heap.insert(10)
heap.insert(14)
heap.insert(8)
heap.insert(7)
heap.insert(22)
heap.insert(5)

print("Extracted minimum:", heap.extractMin())
print("Extracted minimum:", heap.extractMin())

sorted_arr = heap.sort()
print("Sorted array:", sorted_arr)

heap2 = MinHeap()
heap2.insert(5)
heap2.insert(1)
heap2.insert(4)
heap2.insert(2)
heap2.insert(3)

sorted_arr2 = heap2.sort()
print("Sorted array 2:", sorted_arr2)

empty_heap = MinHeap(5)
print("Extract Min from empty heap:", empty_heap.extractMin())