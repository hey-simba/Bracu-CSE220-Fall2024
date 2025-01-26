

class MaxHeap:
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
    while k > 1 and self.heap[k // 2] < self.heap[k]:
      temp = self.heap[k]
      self.heap[k] = self.heap[k // 2]
      self.heap[k // 2] = temp
      k = k // 2

  def extractMax(self):
    if self.size == 0:
      return None
    max_val = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.heap[self.size] = None
    self.size -= 1
    self.sink(1)
    return max_val

  def sink(self, k):
    while 2 * k <= self.size:
      j = 2 * k
      if j < self.size and self.heap[j] < self.heap[j + 1]:
          j += 1
      if self.heap[k] >= self.heap[j]:
          break
      temp = self.heap[k]
      self.heap[k] = self.heap[j]
      self.heap[j] = temp
      k = j

  def sort(self):
    sorted_array = []
    original_size = self.size
    while self.size > 0:
      temp = self.heap[1]
      self.heap[1] = self.heap[self.size]
      self.heap[self.size] = temp
      sorted_array = self.add_to_array(sorted_array, temp)
      self.heap[self.size] = None
      self.size -= 1
      self.sink(1)
    self.size = original_size
    return sorted_array

  def add_to_array(self, arr, val):
    new_arr = [None] * (len(arr) + 1)
    for i in range(len(arr)):
      new_arr[i] = arr[i]
    new_arr[len(arr)] = val
    return new_arr


# Example usage:
heap = MaxHeap(1)
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
print("Extracted maximum:", heap.extractMax())
print("Extracted maximum:", heap.extractMax())

heap.insert(5)

sorted_arr = heap.sort()
print("Sorted array:", sorted_arr)

heap2 = MaxHeap()
heap2.insert(5)
heap2.insert(1)
heap2.insert(4)
heap2.insert(2)
heap2.insert(3)

sorted_arr2 = heap2.sort()
print("Sorted array 2:", sorted_arr2)

empty_heap = MaxHeap(5)
print("Extract Max from empty heap:", empty_heap.extractMax())