class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1, root2):
    # DFS: O(n+m) for time where n,m # of nodes in root1, root2 respectively
    # O(h1 + h2) for space where h1, h2 height of root1, root2 respectively
    # helper function to get the leaf nodes
    # Worst case: a completely unbalanced tree having all nodes as leaves
    def dfs(root, leaf):
        if not root:
            return
        # check if it's a leaf node
        if not root.left and not root.right:
            leaf.append(root.val)
        dfs(root.left, leaf)
        dfs(root.right, leaf)

    leaves1 = []
    leaves2 = []
    # get leaf sequences for both trees
    dfs(root1, leaves1)
    dfs(root2, leaves2)

    # compare the two leaf sequences
    return leaves1 == leaves2
