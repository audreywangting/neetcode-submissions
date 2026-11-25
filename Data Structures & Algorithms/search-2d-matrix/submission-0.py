class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search in 2D
        n = len(matrix) # row
        m = len(matrix[0]) # col
        
        # turn 2D into a sorted 1D
        """
        index:     0  1  2  3 | 4  5  6  7 | 8  9  10 11
        row:       0  0  0  0 | 1  1  1  1 | 2  2   2  2
        col:       0  1  2  3 | 0  1  2  3 | 0  1   2  3
        
        row = index // number_of_columns
        col = index % number_of_columns
        """
        low = 0
        high = (n*m)-1

        # search half n & half m everytime
        while low <= high:
            mid = (low+high)//2
            # 轉成 2D 單純為了取值
            row = mid // m
            col = mid % m

            # 調整 boundary 都用 1D 思考
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1


        return False

            
        