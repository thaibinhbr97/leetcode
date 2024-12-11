def inorderTraversal(root):
    # # left->root->right
    # # recursively
    # res = []

    # def dfs(root, res):
    #     if not root:
    #         return
    #     dfs(root.left, res)
    #     res.append(root.val)
    #     dfs(root.right, res)

    # dfs(root, res)
    # return res

    # iteratively using stack
    res = []
    stack = []
    current = root
    while current or stack:
        # reach the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # current is None here, pop from the stack
        current = stack.pop()
        res.append(current.val)

        # move to the right node after visiting
        current = current.right

    return res
