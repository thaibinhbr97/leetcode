def searchBST(root, val):
    # Recursion
    # T: O(logn) for balanced tree, O(n) for skewed tree
    # S: O(n) for recursive stack
    if not root or root.val == val:
        return root
    if root.val < val:
        return searchBST(root.right, val)
    else:
        return searchBST(root.left, val)


def searchBST(root, val):
    # Iterative
    # T: O(n)
    # S: O(1)
    while root:
        if root.val == val:
            return root
        elif root.val < val:
            root = root.right
        else:
            root = root.left
    return None
