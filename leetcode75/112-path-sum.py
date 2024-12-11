class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: [TreeNode], targetSum: int) -> bool:  # type: ignore
    def dfs(node, sumSoFar):
        if not node:
            return False
        sumSoFar += node.val
        if not node.left and not node.right:
            return sumSoFar == targetSum
        return dfs(node.left, sumSoFar) or dfs(node.right, sumSoFar)

    return dfs(root, 0)
