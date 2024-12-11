def goodNodes(root):
    # O(n) for time, where n is # of nodes in the tree.
    # O(h) for space, where h is height of the tree. Worst case is when completely unbalanced tree -> O(n)
    def dfs(node, max_val):
        # preorder traversal
        if not node:
            return 0

        # check if it is a "good" node (current value >= its ancestor node)
        if node.val >= max_val:
            good = 1
        else:
            good = 0

        # update the max_val for current path
        max_val = max(max_val, node.val)

        # DFS through the left and right children node
        good += dfs(node.left, max_val)
        good += dfs(node.right, max_val)

        return good

    # start DFS from the root where max_val = root.val
    return dfs(root, root.val)
