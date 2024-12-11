import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.minHeap = []
        self.set = set()
        self.current = 1

    def popSmallest(self):
        if self.minHeap:
            smallest = heapq.heappop(self.minHeap)
            self.set.remove(smallest)
        else:
            smallest = self.current
            self.current += 1
        return smallest

    def addBack(self, num):
        if num < self.current and num not in self.set:
            heapq.heappush(self.minHeap, num)
            self.set.add(num)
