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

        """
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


        """
        # optimize: use hash map to quickly get the index->value form inorder
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        # track current root in preorder
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            # base case
            if left > right:
                return None

            # find root from preorder
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            # find root position in inorder
            mid = inorder_idx[root_val]

            # build left subtree
            root.left = build(left, mid-1)

            # build right subtree
            root.right = build(mid+1, right)

            return root

        return build(0, len(preorder)-1)











