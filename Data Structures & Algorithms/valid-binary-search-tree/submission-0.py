# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use dfs helper function to pass on the upper & lower bound since we're passing more arguments

        def dfs(node, low, high):
            # base case:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            # recursion - checking
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float("-inf"), float("inf"))

            

            
