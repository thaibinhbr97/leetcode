import random


class RandomizedSet:

    def __init__(self):
        self.indexMap = {}  # store {value: index}
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.indexMap[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indexMap:
            # the idea is to find the val in the indexMap and swap it with last element
            # in indexMap and remove it to maintain constant time complexity
            last_val = self.values[-1]
            idx = self.indexMap[val]
            # swap with last element
            self.indexMap[last_val] = idx
            self.values[idx] = last_val
            # remove last element
            self.indexMap.pop(val)
            self.values.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
