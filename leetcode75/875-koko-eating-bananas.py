"""
n piles of bananas
piles[i]
h: hours
k: eating speed

each hour, koko chooses some piles of bananas and eat k bananas from the pile

piles = [5,8]
h = 1
k = 6
piles = [8] because 6 > 5 -> so she eats 5 bananas and she will not eat anymore bananas during this h hour

wants to finish eating all bananas before guards return

input: 
piles
h

output:
minimum integer k such that she can eat all bananas within h hours

example:
piles = [3,6,7,11]
h = 8
-> k:4
why?
k = 1, ceil(3/1) + ceil(6/1) + ceil(7/1) + ceil(11/1) = 27 hours >= h | sum(ceil(pile[i]/k)) for i from 0 to n - 1
k = 2, 2 + 3 + 4 + 6 = 15 >= h
k = 3, 1 + 2 + 3 + 4 = 10 >= h
k = 4, 1 + 2 + 2 + 3 = 8 >= h
k = max(piles) = 11, 1 + 1 + 1 + 1 < h

binary search from k = 1 to k = max(piles), everytime we binary search we will get the middle k and use it to compute total=sum(ceil(pile[i]/k))
and check if it <= h. If it is, we move to the right half; if it is not, we move to the left half.
"""

from math import ceil


def computeTotal(piles, k):
    total = 0
    for pile in piles:
        total += ceil(pile / k)
    return total


def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        total = computeTotal(piles, mid)
        if total > h:
            # k is low (koko eating slowly) and it is not possible to complete all bananas
            # increate k by move low to middle point + 1
            low = mid + 1
        else:
            # k is high (koko eating fast) and it is an overkill when eating this fast to complete all bananas
            # decrease k by move high to middle point
            high = mid - 1
    return low


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # 4

piles = [30, 11, 23, 4, 20]
h = 5
print(minEatingSpeed(piles, h))  # 30

piles = [30, 11, 23, 4, 20]
h = 6
print(minEatingSpeed(piles, h))  # 23

piles = [312884470]
h = 312884469
print(minEatingSpeed(piles, h))  # 2
