# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # 遞歸計算左右子樹的最大貢獻值
            left_contribution = max(dfs(node.left), 0)
            right_contribution = max(dfs(node.right), 0)
            
            # 更新包含當前節點的最大路徑和
            current_max = node.val + left_contribution + right_contribution
            
            # 更新全局最大路徑和
            self.max_sum = max(self.max_sum, current_max)
            
            # 返回不包含當前節點的最大貢獻值
            return node.val + max(left_contribution, right_contribution)
        
        # 遞歸計算最大路徑和
        dfs(root)
        
        return self.max_sum
