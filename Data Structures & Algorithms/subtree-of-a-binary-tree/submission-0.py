# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # use dfs to search the possible start, then use isSameTree to check are they the same
        # 1. is the current node same as the subtree's root
        # 2. if not, is the left subtree the same
        # 3. if not, is the right subtree the same

        if root is None:
            return False

        current = self.isSametree(root, subRoot) # subtree就在現在的子樹
        left = self.isSubtree(root.left, subRoot) # subtree就在左子樹
        right = self.isSubtree(root.right, subRoot) # subtree就在右子樹
        return current or left or right
        

    def isSametree(self, p, q):
        # for helping to check if the nodes in 2 trees are the same
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        left = self.isSametree(p.left, q.left)
        right = self.isSametree(p.right, q.right)

        return left and right