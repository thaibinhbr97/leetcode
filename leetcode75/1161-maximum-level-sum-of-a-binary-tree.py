import math
from collections import deque


def maxLevelSum(root):
    if not root:
        return
    maxSoFar = -math.inf
    sumLevel = []
    q = deque()
    q.append(root)
    while q:
        qLen = len(q)
        total = 0  # reset total every level
        for i in range(qLen):
            node = q.popleft()
            total += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        sumLevel.append(total)
        maxSoFar = max(maxSoFar, total)

    for i in range(len(sumLevel)):
        if maxSoFar == sumLevel[i]:
            return i + 1
