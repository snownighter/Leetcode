# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        visited = set()

        def travel(root):
            if not root:
                return False
            val = k - root.val
            if val in visited:
                return True
            else:
                visited.add(root.val)
                return travel(root.left) or travel(root.right)

        return travel(root)
        
