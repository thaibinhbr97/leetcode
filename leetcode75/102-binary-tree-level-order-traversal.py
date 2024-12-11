class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import queue


def levelOrder(root):
    ans = []
    if not root:
        return ans
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        qLen = q.qsize()
        level = []  # sublist for each level
        for i in range(qLen):
            node = q.get()
            if node:
                level.append(node.val)
                q.put(node.left)
                q.put(node.right)
        if level:
            ans.append(level)
    return ans


from collections import deque


def levelOrder(root):
    result = []
    if not root:
        return result
    q = deque()
    q.append(root)
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            result.append(level)
    return result
