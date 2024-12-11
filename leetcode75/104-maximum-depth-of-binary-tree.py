class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepthDFS(root):
    # base case: if root has no left or right child, the depth is 0
    if root == None:
        return 0
    # recursively find the left and right subtrees
    leftDepth = maxDepthDFS(root.left)
    rightDepth = maxDepthDFS(root.right)
    # maximum depth is 1 (depth for the current node) + the greater of two subtrees depths
    return 1 + max(leftDepth, rightDepth)


from collections import deque


def maxDepthBFS(root):
    # O(n) for space, time
    if not root:
        return 0
    q = deque([root])
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def maxDepthIterative(root):
    if not root:
        return 0
    stack = [(root, 1)]
    res = 1
    while stack:
        node, level = stack.pop()
        if node:
            res = max(res, level)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
    return res
