# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order turn the tree into sorted array then use index k-1 to find the value?
        """
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
        """
        # opimize：用count = k 代表走到了kth 小元素，不需要遍歷完整個tree

        count = 0 
        ans = None

        def inorder(node):
            nonlocal count, ans
            # base case
            if not node or ans is not None:
                return 

            # L
            inorder(node.left)
            
            # D
            count += 1
            if count == k:
                ans = node.val
                return 

            # R
            inorder(node.right)

        inorder(root)

        return ans
            



