class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    ans = []

    def dfs(node, curPath, curSum):
        if not node:
            return

        curPath.append(node.val)
        curSum += node.val

        # check if curSum equals to targetSum and if the path has reached the leaf node
        if curSum == targetSum and not node.left and not node.right:
            # add a copy of curPath to ans since curPath is mutable after each recursive call
            ans.append(list(curPath))

        dfs(node.left, curPath, curSum)
        dfs(node.right, curPath, curSum)

        # backtracking by removing the current node to the path before returning to the previous call
        curPath.pop()

    dfs(root, [], 0)
    return ans
