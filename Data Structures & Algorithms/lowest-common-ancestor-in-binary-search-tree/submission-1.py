# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # since it's binary search tree, use the order to judge
        # if root should be between p & q to become LCA
        # if root < p & q -> LCA is on the right
        # if root > p & q -> LCA is on the left
        
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left

            elif root.val < p.val and root.val < q.val:
                root = root.right

            else:
                return root


