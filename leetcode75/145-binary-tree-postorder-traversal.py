# left->right->node


# recursive
def postorderTraversal(root):
    res = []
    if not root:
        return res

    def dfs(node, res):
        if not node:
            return
        dfs(node.left, res)
        dfs(node.right, res)
        res.append(node.val)

    dfs(root, res)
    return res


# iteratively using 1 stack
def postorderTraversal(root):
    stack = [root]
    visited = [False]
    res = []
    while stack:
        cur = stack.pop()
        v = visited.pop()
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visited.append(True)
                stack.append(cur.right)
                visited.append(False)
                stack.append(cur.left)
                visited.append(False)

    return res


def postorderTraversal(root):
    # left->right->root
    # similar to pre but in reverse
    # pre: root->left->right (1)
    # reverse post => root->right->left (2)
    # so we do root->right->left then reverse it to left->right->root to solve this.
    ans = []
    if not root:
        return ans
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # reverse ans to get the solution for this problem (from root->right->left to left->right->root)
    ans.reverse()
    return ans


# left->right->root
# iteratively using 2 stack
# two-stack approach uses the first stack for tree traversal and the second stack to reverse the order,
# resulting in a postorder traversal
def postorderTraversal(root):
    ans = []
    if not root:
        return ans
    # stack1 holds nodes for traversal in a reversed-preorder order
    stack1 = [root]
    # stack2 stores nodes in the sequence they should be visited in postorder
    # -> left->right->root
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        # building root->right->left stack and pop at the end to get left->right->root as ans
    while stack2:
        ans.append(stack2.pop())
    return ans
