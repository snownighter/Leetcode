# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node, prev):
            if not node:
                return True

            #print(prev)
            
            # 遞歸處理左子樹
            if not inorder(node.left, prev):
                #print('f1')
                return False
            
            # 檢查節點值是否遞增
            if node.val <= prev[0]:
                #print(node.val, prev[0], 'f2')
                return False
            prev[0] = node.val
            
            # 遞歸處理右子樹
            return inorder(node.right, prev)
        
        # 開始中序遍歷
        prev = [float('-inf')]
        return inorder(root, prev)
