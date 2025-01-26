
#using already created MaxHeap class
def find_k_largest(nums, k):
    n = len(nums)
    heap = MaxHeap(n)
    for i in range(n):
        heap.insert(nums[i])
    result = np.zeros(k, dtype=int)
    for i in range(k):
        result[i] = heap.extractMax()

    return result

nums = [4, 10, 2, 8, 6, 7]
k = 3
result = find_k_largest(nums, k)
print("Top k largest elements:", result)