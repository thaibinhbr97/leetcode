from collections import deque


def rightSideView(root):
    # BFS
    # O(n) for time, O(n) for space
    ans = []
    if not root:
        return ans
    q = deque()
    q.append(root)
    while q:
        qLen = len(q)
        rightIndex = qLen - 1
        for i in range(qLen):
            node = q.popleft()
            if i == rightIndex:
                ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans


def rightSideView(root):
    # DFS
    # O(n) for time, O(n) for space
    res = []

    def dfs(root, depth):
        if not root:
            return
        # if we are at a new depth level, append the right node to the result by recursing the right node first
        if depth == len(res):
            res.append(root.val)
        dfs(root.right, depth + 1)
        dfs(root.left, depth + 1)

    dfs(root, 0)
    return res
