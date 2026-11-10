# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order turn the tree into sorted array then use index k-1 to find the value?

        arr = []

        # in-order, dfs
        def inorder(node):
            # base case
            if not node:
                return 

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

            return arr

        inorder(root)

        return arr[k-1]
