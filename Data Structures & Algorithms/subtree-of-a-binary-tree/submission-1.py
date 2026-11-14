# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # use helper function - isSameTree to check if the subtree is the same
        # use recursion to keep seeing if the current node is the root to start or left or right

        def isSameTree(p, q):
            # base case
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False
            
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right
        
        # base case
        if not root:
            return False

        # recursion
        # 1. check current
        if isSameTree(root, subRoot):
            return True

        # explore left & right
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right



            