from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs, use deque to store
        # initialize the queue with root inside, and add its child if exists

        queue = deque([root])
        result = []

        if not root:
            return []

        while queue:
            level_size = len(queue)
            level = [] # 記錄這一層的元素

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

                

