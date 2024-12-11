def longestZigZag(root):
    maxLen = 0

    def dfs(node, lastMove, length):
        if not node:
            return
        maxLen = max(maxLen, length)
        if lastMove == "left":
            dfs(node.right, "right", length + 1)
            dfs(node.left, "left", 1)
        else:
            dfs(node.left, "left", length + 1)
            dfs(node.right, "right", 1)

    dfs(root, "left", 0)
    dfs(root, "right", 0)
    return maxLen


# def longestZigZag(root):
#     self.maxLen = 0

#     def dfs(node, lastMove, length):
#         if not node:
#             return
#         self.maxLen = max(self.maxLen, length)
#         if lastMove == "left":
#             dfs(node.right, "right", length + 1)
#             dfs(node.left, "left", 1)
#         else:
#             dfs(node.left, "left", length + 1)
#             dfs(node.right, "right", 1)

#     dfs(root, "left", 0)
#     dfs(root, "right", 0)
#     return self.maxLen
