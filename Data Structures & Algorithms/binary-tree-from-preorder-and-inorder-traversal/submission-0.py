# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use preorder: find the root
        # use inorder: find the left subtree & right subtree
        # use dfs to kerep building the binary tree

        def build(preorder, inorder):
            # base case
            if not preorder:
                return 

            # get the root
            root_val = preorder[0]
            root = TreeNode(root_val)

            # get the root's index in inorder, to seperate left & right subtree
            mid = inorder.index(root_val)

            # build left subtree
            root.left = build(preorder[1:mid+1], inorder[:mid])
            # build right subtree
            root.right = build(preorder[mid+1:], inorder[mid+1:])

            return root

        return build(preorder, inorder)


