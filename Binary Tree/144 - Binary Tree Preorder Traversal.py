# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)



#iterative preorder using stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if not root:
        return []

    stack = [root]        # Start with root
    result = []

    while stack:
        node = stack.pop()      # Step 1: Pop top node
        result.append(node.val) # Step 2: Process node

        # Step 3: Push children (right first, then left)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

