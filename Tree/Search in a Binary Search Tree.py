# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None:
        return None
    elif root.val == val:
        return root
    else:
        if root.val < val:
            return searchBST(root.right, val)
        else:
            return searchBST(root.left, val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return searchBST(root, val)
