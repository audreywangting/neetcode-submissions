class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search since it's a increasing list
        # then use col + row to find the target
        # treat matrix as a 1D array

        # index: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        # row: 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2 -> index//col
        # col: 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 -> index%col

        m = len(matrix) # row
        n = len(matrix[0]) #col

        left = 0
        right = n*m - 1

        while left <= right:
            mid = (left+right) //2
            row = mid//n
            col = mid%n
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False

            


