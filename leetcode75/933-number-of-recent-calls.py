import queue


# using deque
class RecentCount:
    def __init__(self):
        self.q = queue.deque()
        self.count = 0

    def ping(self, t):
        self.q.appendd(t)
        self.count += 1

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.count -= 1

        return self.count


# using queue
class RecentCounter:
    def __init__(self):
        self.q = queue.Queue()
        self.count = 0

    def ping(self, t):
        self.q.put(t)
        self.count += 1

        while self.q and self.q.queue[0] < t - 3000:
            self.q.get()
            self.count -= 1

        return self.count


obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
