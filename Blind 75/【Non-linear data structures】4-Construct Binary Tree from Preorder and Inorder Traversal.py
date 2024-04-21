# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # 使用字典存儲中序遍歷序列中每個節點的索引位置
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build_helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍歷序列中的第一個節點是根節點
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            
            # 在中序遍歷序列中找到根節點的索引位置
            inorder_root_idx = inorder_map[root_val]
            
            # 左子樹的範圍：中序遍歷序列中根節點左側的節點
            left_subtree_size = inorder_root_idx - inorder_left
            root.left = build_helper(preorder_left + 1, preorder_left + left_subtree_size, inorder_left, inorder_root_idx - 1)
            
            # 右子樹的範圍：中序遍歷序列中根節點右側的節點
            root.right = build_helper(preorder_left + left_subtree_size + 1, preorder_right, inorder_root_idx + 1, inorder_right)
            
            return root
        
        return build_helper(0, len(preorder) - 1, 0, len(inorder) - 1)
