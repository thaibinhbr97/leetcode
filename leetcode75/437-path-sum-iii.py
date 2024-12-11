from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    # # O(n^2) for time, O(h) for space
    # # Brute force (DFS for each node)
    # if not root:
    #     return 0

    # def dfs(node, curSum):
    #     if not node:
    #         return 0
    #     curSum += node.val

    #     return (curSum == targetSum) + dfs(node.left, curSum) + dfs(node.right, curSum)

    # return dfs(root, 0) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)

    # Optimized approach using prefix sum and hashmap
    prefixSumCount = defaultdict(int)
    prefixSumCount[0] = 1  # handle cases where the sum equals targetSum from the root

    def dfs(node, curSum):
        if not node:
            return 0

        curSum += node.val

        # check how many times prefix sum satisfies the condition
        # if curSum - targetSum exists in the hash map, there is a path
        # from an earlier node to the current node that sums to targetSum
        pathCount = prefixSumCount[curSum - targetSum]
        prefixSumCount[curSum] += 1
        pathCount += dfs(node.left, curSum)
        pathCount += dfs(node.right, curSum)
        # backtrack by removing the current cumulative sum from the hash map
        # when moving back up the tree. This ensures that when returing from a node,
        # we don't accidentally reuse its sum in a different path
        # prefixSumCount[curSum] -= 1

        return pathCount

    return dfs(root, 0)


root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
targetSum = 8
print(pathSum(root, targetSum))
