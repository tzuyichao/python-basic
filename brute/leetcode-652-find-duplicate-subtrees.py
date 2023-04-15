# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        store = dict()
        res = []
        self.helper(root, store, res)
        return res
    
    def helper(self, node, store, res):
        if node is None:
            return "#"
        s = str(node.val) + "," + self.helper(node.left, store, res) + "," + self.helper(node.right, store, res)
        if s in store and store[s] == 1:
            res.append(node)
        if s in store:
            store[s] = store[s]+1
        else:
            store[s] = 1
        return s
        