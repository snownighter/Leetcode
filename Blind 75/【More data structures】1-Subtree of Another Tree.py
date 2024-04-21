# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # 定義深度優先搜索函數
        def dfs(s, t):
            # 如果兩棵樹都是空樹，則返回 True
            if not s and not t:
                return True
            # 如果其中一棵樹是空樹，則返回 False
            if not s or not t:
                return False
            # 如果兩棵樹的根節點值不相等，則返回 False
            if s.val != t.val:
                return False
            # 遞歸檢查左子樹和右子樹
            return dfs(s.left, t.left) and dfs(s.right, t.right)
        
        # 遍歷原始樹的每個節點，對每個節點進行比較
        def traverse(s, t):
            if not s:
                return False
            # 如果找到與目標樹根節點值相同的節點，則進行深度優先搜索比較
            if s.val == t.val and dfs(s, t):
                return True
            # 否則繼續遍歷左子樹和右子樹
            return traverse(s.left, t) or traverse(s.right, t)
        
        return traverse(root, subRoot)
