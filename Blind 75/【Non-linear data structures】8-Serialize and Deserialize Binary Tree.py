# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return "None,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)
        
        return preorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            if nodes[0] == "None":
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes[0]))
            nodes.pop(0)
            root.left = build_tree(nodes)
            root.right = build_tree(nodes)
            return root
        
        nodes = data.split(",")
        return build_tree(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
