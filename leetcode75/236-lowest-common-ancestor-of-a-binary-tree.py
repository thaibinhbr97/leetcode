def lowestCommonAncestor(root, p, q):
    # O(n) for time, O(n) for space (recursive stack) | O(1) without recursive stackl
    # return LCS give a binary tree
    # 1. p and q are in opposite side of the binary tree -> return the root node that has these two nodes as descendent (LCA)
    # 2. p is parent of q (q is a descendant) -> return p because p itself is a LCA of itself and q
    # 3. q is parent of q (p is a descentdant) -> ...
    if root == None or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are non-null, current node is the LCA
    if left and right:
        # root as LCA
        return root
    # otherwise, return non-null child (could be an ancestor or null if not found)
    return left or right
