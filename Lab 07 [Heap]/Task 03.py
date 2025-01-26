
#using already created MinHeap class
def distribute_tasks(tasks, m):
    heap = MinHeap(m)

    for _ in range(m):
        heap.insert(0)

    for task in tasks:
        min_load = heap.extractMin()
        updated_load = min_load + task
        heap.insert(updated_load)
    sorted_heap = sorted(heap.heap[1:heap.size + 1])
    return sorted_heap

tasks = [2, 4, 7, 1, 6]
m = 4
result = distribute_tasks(tasks, m)
print("Result:", result)