def deleteNode(root, key):
    if not root:
        return None
    # locate node with a key
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # if key found, there are 3 cases
        # 1. node to delete has no children (leaf node)
        if not root.left and not root.right:
            return None
        # 2. node to delete has 1 child
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left

        # 3. node to delete has two children
        # either find inorder successor(smallest node in the right subtree)
        # or inorder predecessor(largest node in left subtree)
        target_node = findMin(root.right)
        root.val = target_node.val
        root.right = deleteNode(root.right, target_node.val)
    return root


def findMin(node):
    while node.left:
        node = node.left
    return node


def deletNode(root, key):
    if not root:
        return None

    # locate the key
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # key is found here, we need to delete the node
        # 3 cases
        # 1. deleted node has 0 children
        if not root.left and not root.right:
            return None
        # 2. deleted node has 1 child
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        # 3. deleted node has 2 children
        # we will use inorder predecessor (largest node in left subtree) to replace the node to be deleted
        # since largest node in the left subtree is on the very right and down on that left subtree
        # we will need to use the helper function called findMax to get that node.
        # Once we have the location of that node, we can replace the deleted node with that node
        # Then, we keep deleting remaining nodes on the left of the root since we use inorder predecessor
        targetNode = findMax(root.left)
        root.val = targetNode.val
        root.left = deleteNode(root.left, targetNode.val)
    return root


def findMax(root):
    while root.right:
        root = root.right
    return root
