"""
input:
costs: List[int] -> array of cost
costs[i]: int -> the cost of hiring ith worker
k: int -> a number of workers we want to hire
candidates: int -> 

rules:
run k sessions and hire exactly one worker in each session
in each hiring session, choose lowest cost from first candidates and last candidates. If their cost are the same, pick the
lowest index

take away:
When workers have the same cost, we will pick the one with the lowest index -> keep track of indexing (maybe using tuple
that take the cost as the first parameter and index as the second parameter and we will use heap to store the lowest cost)

costs = [2,1], candidates = 3 -> find the lowest cost

output:
total cost to hire k workers

example:
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

algorithm
since we need to take candidates from each left and right poold and we use two min heaps for each pool and two pointer left and right to add it to these 
min heaps
"""

import heapq


def totalCost(costs, k, candidates):
    # time: O(candidates * log(candidates) + k * log(candidates)) => O([k+candidates]*log(candidates)
    # space: candidates for heaps
    n = len(costs)
    left = 0
    right = n - 1
    leftPool = []
    rightPool = []
    sumCost = 0
    INF = float("inf")
    while k > 0:
        while len(leftPool) < candidates and left <= right:
            heapq.heappush(leftPool, costs[left])
            left += 1
        while len(rightPool) < candidates and right >= left:
            heapq.heappush(rightPool, costs[right])
            right -= 1
        leftMin = leftPool[0] if len(leftPool) > 0 else INF
        rightMin = rightPool[0] if len(rightPool) > 0 else INF
        if leftMin <= rightMin:
            sumCost += leftMin
            heapq.heappop(leftPool)
        else:
            sumCost += rightMin
            heapq.heappop(rightPool)
        k -= 1
    return sumCost


costs = [10, 20, 15, 30, 40]
k = 3
candidates = 2
print(totalCost(costs, k, candidates))  # 45

costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
print(totalCost(costs, k, candidates))  # 11


costs = [1, 2, 4, 1]
k = 3
candidates = 3
print(totalCost(costs, k, candidates))  # 4


costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
k = 11
candidates = 2
print(totalCost(costs, k, candidates))  # 423

costs = [
    28,
    35,
    21,
    13,
    21,
    72,
    35,
    52,
    74,
    92,
    25,
    65,
    77,
    1,
    73,
    32,
    43,
    68,
    8,
    100,
    84,
    80,
    14,
    88,
    42,
    53,
    98,
    69,
    64,
    40,
    60,
    23,
    99,
    83,
    5,
    21,
    76,
    34,
]
k = 32
candidates = 12
print(totalCost(costs, k, candidates))  # 1407
