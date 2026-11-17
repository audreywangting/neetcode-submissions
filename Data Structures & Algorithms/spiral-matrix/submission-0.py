class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 不斷往內縮
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = [] #matrix[row][col]

        while top <= bottom and left <= right:
            
            # 1. top row: left -> right 
            for c in range(left, right+1):
                result.append(matrix[top][c])
            top += 1

            # 2. right col: top -> down
            for r in range(top, bottom+1):
                result.append(matrix[r][right])
            right -= 1
            
            # 3. bottom row: right -> left
            if top <= bottom:
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            # 4. left col: down -> top
            if left <= right:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
            



