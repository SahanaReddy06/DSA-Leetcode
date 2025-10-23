# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        res = []

        # Function to check if a node is a leaf
        def isLeaf(node):
            return not node.left and not node.right

        # Add left boundary (excluding leaves)
        def addLeft(node):
            while node:
                if not isLeaf(node):
                    res.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # Add all leaf nodes (using DFS)
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.val)
            addLeaves(node.left)
            addLeaves(node.right)

        # Add right boundary (excluding leaves)
        def addRight(node):
            temp = []
            while node:
                if not isLeaf(node):
                    temp.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            # reverse before adding to main list
            res.extend(temp[::-1])

        # Root
        if not isLeaf(root):
            res.append(root.val)

        # Left boundary
        addLeft(root.left)

        # Leaf nodes
        addLeaves(root)

        # Right boundary
        addRight(root.right)

        return res
