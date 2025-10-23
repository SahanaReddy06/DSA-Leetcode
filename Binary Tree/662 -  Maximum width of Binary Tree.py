from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width=0
        queue=deque([(root,0)])  # node, index)
        while queue:
            _, left=queue[0]     #leftmost index     _. it takes node and index, since index is most need here
            _, right=queue[-1]   #rightmost 
            max_width=max(max_width,right-left+1)

            for _ in range(len(queue)):   
                node, idx=queue.popleft()
                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx+1))
    
        return max_width
