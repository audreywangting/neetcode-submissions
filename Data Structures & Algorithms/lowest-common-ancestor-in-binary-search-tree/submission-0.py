# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST to compare val
        # if current node > p and > q: left to find LCA
        # if current node < p and < q: right to find LCA
        # else: we found LCA

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left

            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root
