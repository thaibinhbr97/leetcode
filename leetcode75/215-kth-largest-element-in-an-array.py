from queue import PriorityQueue

"""
Time:
build a heap: O(n) for time, O(1) if in place and O(logn) for recursive heapifyfor the call stack give a binary tree
find a max or min element in a heap: O(1)
add an element into a heap: O(logn)
remove an element from a heap: O(logn)
"""


def findKthLargest(nums, k):
    """
    since we need to find the kth largest elements, initial idea is to use heap to find it

    idea:
    change original heap from min heap to max heap to find the kth largest given nums and k

    Time: O(n*log(n)), n is a number of elements in array nums
    """

    class MaxHeap:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value > other.value

        def getValue(self):
            return self.value

    max_heap = PriorityQueue()
    for num in nums:  # O(n)
        max_heap.put(MaxHeap(num))  # O(logn)
    i = 0
    while i < k:  # O(n)
        element = max_heap.get()  # O(1)
        i += 1
    return element.getValue()


import heapq


def findKthLargestHeapq(nums, k):
    class MaxHeap:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value > other.value

        def getValue(self):
            return self.value

    # create a max heap and keep poping from the heap until reaching k (for k largest element)
    # time: O(nlogk), n is the size of arr and k is the size of the heap
    # space: O(k), k is the size of the heap
    h = []
    for num in nums:  # O(n)
        heapq.heappush(h, MaxHeap(num))  # O(logk)
    i = 0
    while i < k:  # O(k)
        element = heapq.heappop(h)  # O(logk)
        i += 1
    return element.value

    # using min heap and keep poping as long as heap length > k. Then, the first element will be the kth largest element
    # time: O(nlogk), n is the sie of the array and k is the size of the heap
    # space: O(k)
    h = []
    for num in nums:  # O(n), n is the size of array nums
        heapq.heappush(h, num)  # O(logk), k is the size of the heap
        if len(h) > k:
            heapq.heappop(h)  # O(logk), k is the size of the heap
    return h[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
print(findKthLargestHeapq(nums, k))
"""
max_heap = [6, 5, 4, 3, 2, 1]
result_arr = [6, 5]
ans = 5 = result_arr[-1] = max_heap[0] # after popping k-1 element
"""
