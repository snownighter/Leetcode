# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 如果 p 和 q 的值都小於當前節點的值，則最低公共祖先在當前節點的左子樹中
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # 如果 p 和 q 的值都大於當前節點的值，則最低公共祖先在當前節點的右子樹中
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # 其他情況下，當前節點就是最低公共祖先
        else:
            return root
