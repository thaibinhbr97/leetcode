# # using recursion
# def preorderTraversal(root):
#     res = []

#     def dfs(root, res):
#         if not root:
#             return
#         res.append(root.val)
#         dfs(root.left, res)
#         dfs(root.right, res)

#     dfs(root, res)
#     return res


# using stack
def preorderTraversal(root):
    # root->left->right
    res = []
    if not root:
        return res
    s = [root]

    while s:
        node = s.pop()
        res.append(node.val)
        # append the right node right then left node to ensure the stack popping the left node first to the res as in preorder
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return res
